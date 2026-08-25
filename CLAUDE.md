# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概览

**规范查询 skill 工程**:一个 Claude Code skill(`guifan-chaxun`),让 agent 按"翻书"方式查询中国工程规范 PDF——书架 → 目录 → 章节 → 条文原文。**不做向量库**,全部索引产物是文件系统上的明文(可 grep、可 Read)。试点 15 本(guifansrc),实际规模 200+ 本,设计支持批量扩展。

**两态模型**:①查询态——按索引翻书查规范(纯文件操作,零 Python);②维护态——库有增删时先更新索引再查询(增=index、删=remove、换版=标记替代),**该 OCR 就 OCR**。

## 常用命令(开发/维护视角)

skill 唯一程序是 `scripts/spec.py`(10 子命令),依赖 pymupdf + tesseract(路径与语言包在 `config.json`):

```bash
# 维护态
python spec.py index <PDF...> | --all [--force] [--jobs N]   # 加书/建索引(质量检测→[OCR]→目录→切章→条文索引)
python spec.py status                                         # 库一致性检查(新书/失效/换版)+ 书架健康
python spec.py ocr <book> [--start N] [--end N]               # 整本批量 OCR(断点续跑,index 内部也会调)
python spec.py remove <book> [--mark-superseded <新id>]       # 删索引/登记,或标记被替代(不物理删)
python spec.py update-chars --from-pdfs <干净文字版PDF...>    # 重建常用字表(乱码检测资源,新领域书先跑)

# 查询态(纯文件;agent 走 SKILL.md 流程,这些是 CLI 调试用)
python spec.py list [-q 关键词] / toc <book> / clause <book> <条文号> / read <book> <页> / grep <book> <正则> | --all
```

- Python 3.12(`python` 命令);tesseract 5.4 装于 `C:\Program Files\Tesseract-OCR\`,chi_sim 语言包在 `scripts/tessdata/`(config `ocr_tessdata_dir` 指向,自包含)。
- 控制台 GBK:spec.py 内部已 `sys.stdout.reconfigure(utf-8)`;自己写临时脚本加 `PYTHONIOENCODING=utf-8`。

## 架构

```
guifanchaxun/
├── .claude/skills/guifan-chaxun/     # skill 本体
│   ├── SKILL.md                      # 查询/维护工作流(两态)、强制学习、禁令
│   ├── config.json                   # library_dir(PDF 源)/ data_dir(索引)/ OCR 参数——换库唯一改动点
│   ├── scripts/spec.py               # 唯一程序,全部子命令与流水线
│   ├── scripts/common_chars.txt      # ~3500 常用字表(乱码检测资源)
│   ├── scripts/tessdata/             # chi_sim 语言包(自包含)
│   └── references/
│       ├── pdf_reading.md            # 强制学习方法文档(处理 PDF 前必读)
│       └── query_notes.md            # 场景化防漏清单(作业区布设等,实战易漏项沉淀)
└── library_data/                     # 索引数据(bookshelf.json + 每书一个目录)
```

**数据布局**(`library_data/<book_id>/`):`meta.json`(元数据+probe 证据+chapter_list)、`toc.md`(章节索引表,查询导航核心)、`clauses.idx`(条文号→页码 TSV,含 expl/ocr/低置信标记)、`chapters/chNN-*.md`(分章全文,头部注释含页码/条文号范围,正文每页前有 `【第 N 页】`)、`ocr/NNN.txt`(仅 OCR 书,唯一文本来源)。

**book_id 规则**:`= 源文件名去 .pdf`(如 `1.公路桥涵养护规范(JTG 5120-2021)`),与 guifansrc 里的规范原名一一对应。**guifansrc 支持多层文件夹**:`file` 字段存相对 library_dir 的路径(`rglob` 递归收集,`status` 一致性检查用相对路径键避免同名混淆);同名不同路径时 book_id 加父目录前缀。**人工元数据优先**:`_index_one` 里若 bookshelf 已有同源文件条目,则 std_no/title/version/id 以书架为准(文件名没写编号的书,人工在 bookshelf.json 补 std_no 即可,如 6.公路隧道养护技术规范 的 std_no=JTG 5130—2026)。

## 关键设计决策(改代码勿重蹈)

1. **文字书不落盘 pages/**(方案 A):提取在内存聚合,`read` 现场从 PDF 提取;OCR 书的 `ocr/` 必须保留(它是 OCR 原始产物,章文件/条文索引都从它生成)。改 extract/load 逻辑时注意两者读源不同。
2. **质量检测三信号**(`probe_pdf`):无字页占比(扫描)、常用字覆盖率<0.95、标点污染率>0.08 且劣化页>60%(乱码)。GB 5768 系列有**两种乱码模式**(A:汉字可读但数字→符号、覆盖率 0.85-0.94;B:全乱、覆盖率 0),单信号抓不全,双信号+条文号命中仲裁缺一不可。封面/公告/目录页(前 5 页)只参与扫描判定,不参与覆盖率。
3. **TOC 三路径回退**:书签(存在 page=-1 即弃)→ 目录页解析(区段检测:带"目次/目录"标记+目录行密度;**正文页信号截断**;页码"- 1 -"残缺用章标题回正文定位+偏移校准)→ 正文扫描/条文号聚类。**OCR 书一律走"条文号聚类定页+顺序补章"**(`clause_cluster`),目录页解析结果不可信。
4. **条文说明三种排版**:独立末章(书后半部+页首"条文说明"+同页重新从第 1 章编号才判)、随条文内嵌(不建章)、无。clauses.idx 里条文说明区条目标 expl=1(clause 直查双命中)。
5. **OCR 数字混淆归一化**(`OCR_NORM_TABLE`):s/S→5、l/I/丨→1、O/o→0、$^→去符号。GB 5768.9-2025 等新版条文号**跨行排版**("4." 行 + 下一行 "5" = 4.5),`build_clauses` 有跨行组合(标 low 置信)。
6. **并发写 bookshelf 竞态**:`index --jobs N` 并行时 `_index_one` **不写 bookshelf.json**,`cmd_index` 在单线程合并结果再写;`_index_one` 返回 `(path, status, msg, entry)` 四元组。
7. **章文件后缀 .md**:`write_chapters` 清理时兼容 `*.txt`+`*.md`;grep/status 的 glob 同兼容。toc.md 里章文件引用同步。
8. **控制台/Windows**:路径含中文/全角括号必须引号;文件名首尾空格、全角破折号"—"是合法字符;`\xa0`/`\u3000` 是规范 PDF 的合法标题分隔符,正则字符类必须包含。
9. **常见正则**:条文号 `^\d{1,2}\.\d{1,2}(?:\.\d{1,3})?(?=空白|汉字)`(排除裸数字行列项);章标题兼容同行/粘连/独立数字行三种排版。

## 扩展约定

- **新书入库**:PDF 放 `library_dir` → `spec.py index --all`(增量,mtime 未变自动跳过;OCR 书断点续跑)。文件名带序号前缀(`N.名称(编号).pdf`)。
- **新领域扩展**:常用字表可能覆盖不全 → `spec.py update-chars` 重新生成;`bookshelf.json` 补 category/alias/替代关系。
- **实战易漏项沉淀**:每次查询踩到漏项,追加到 `references/query_notes.md` 对应场景的"易漏项"小节;新场景按同格式新建小节(该文件是防漏机制,SKILL.md 工作流步骤 4 引用它)。
- **查询用法文档**:agent 使用姿势在 `SKILL.md`(两态工作流/输出格式/禁令),改 SKILL.md 时保持与 spec.py 实际行为一致。
