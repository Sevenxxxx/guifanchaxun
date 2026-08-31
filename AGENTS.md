# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 项目概览

**规范查询 skill 工程**:一个 Codex skill(`guifan-chaxun`),让 agent 按"翻书"方式查询中国工程规范 PDF 及库内公文/通知等知识文件——书架 → 目录 → 章节 → 条文原文。**不做向量库**,全部索引产物是文件系统上的明文(可 grep、可 Read)。实际规模 530+ 本 PDF + 350+ 个非 PDF 知识文件(guifansrc),设计支持批量扩展。

**两态模型**:①查询态——按索引翻书查规范(纯文件操作,零 Python);②维护态——库有增删时先更新索引再查询(增=index、删=remove、换版=标记替代),**该 OCR 就 OCR**。

## 常用命令(开发/维护视角)

skill 唯一程序是 `tools/guifan-chaxun-scripts/scripts/spec.py`(13 子命令:index/list/toc/clause/read/grep/ocr/status/remove/update-chars/img/recheck/set-page),依赖 pymupdf + tesseract(路径与语言包在 `config.json`):

```bash
# 以下命令在 tools/guifan-chaxun-scripts/ 目录下执行(python scripts/spec.py ...);
# 从仓库根跑用全路径 python tools/guifan-chaxun-scripts/scripts/spec.py ...

# 维护态
python scripts/spec.py index <文件...> | --all [--force] [--jobs N] [--only ext...]  # 加书/建索引(质量检测→[OCR]→目录→切章→条文索引)
python scripts/spec.py status                                         # 库一致性检查(新书/失效/换版/未索引格式)+ 书架健康
python scripts/spec.py ocr <book> [--start N] [--end N]               # 整本批量 OCR(断点续跑,index 内部也会调;图片书同构)
python scripts/spec.py remove <book> [--mark-superseded <新id>]       # 删索引/登记,或标记被替代(不物理删)
python scripts/spec.py update-chars --from-pdfs <干净文字版PDF...>    # 重建常用字表(乱码检测资源,新领域书先跑)
python scripts/spec.py index <源文件> --rebuild                       # 从已有文本重建章/条文/目录(不重 OCR;视觉修正后生效)
python scripts/spec.py img <book> <页>                                # 渲染源 PDF 页为 PNG(供 agent 视觉复核)
python scripts/spec.py recheck <book>                                 # 报告低置信/失败页(视觉复核清单)
python scripts/spec.py set-page <book> <页> --text "..."              # 回写修正后页文本(配合 index --rebuild)

# 查询态(纯文件;agent 走 SKILL.md 流程,这些是 CLI 调试用)
python scripts/spec.py list [-q 关键词] / toc <book> / clause <book> <条文号> / read <book> <页> / grep <book> <正则> | --all
```

- Python 3.12(`python` 命令);tesseract 5.4 装于 `C:\Program Files\Tesseract-OCR\`,chi_sim 语言包在 `tools/guifan-chaxun-scripts/scripts/tessdata/`(config `ocr_tessdata_dir` 指向,自包含)。
- **多格式支持**:pdf 走 pymupdf;docx/xlsx 纯 Python(python-docx/openpyxl);doc/xls/wps/et 老格式经本机 Office 2021/WPS 12.1 COM 另存后解析(**COM 串行,严禁进线程池**);ofd 纯 Python 读 XML 文本层;png/tif 走 tesseract。zip 不索引(status 提示)。
- 控制台 GBK:spec.py 内部已 `sys.stdout.reconfigure(utf-8)`;自己写临时脚本加 `PYTHONIOENCODING=utf-8`。

## 架构

```
guifanchaxun/
├── tools/
│   ├── guifan-chaxun/                # skill 本体(经软链 ~/.Codex/skills/guifan-chaxun 加载)
│   │   ├── SKILL.md                  # 查询/维护工作流(两态)、强制学习、禁令
│   │   └── references/
│   │       ├── pdf_reading.md        # 强制学习方法文档(处理 PDF 前必读)
│   │       └── query_notes.md        # 场景化防漏清单(作业区布设等,实战易漏项沉淀)
│   └── guifan-chaxun-scripts/        # 脚本与配置
│       ├── config.json               # library_dir(PDF 源)/ data_dir(索引)/ OCR 参数——换库唯一改动点
│       └── scripts/
│           ├── spec.py               # 唯一程序,全部子命令与流水线
│           ├── common_chars.txt      # ~3500 常用字表(乱码检测资源)
│           └── tessdata/             # chi_sim 语言包(自包含)
├── scripts/Codex-hooks/             # 提交前审查 hook(pre-commit-review.sh + check_commit.py)
├── library_data/                     # 索引数据(bookshelf.json + 每书一个目录)
└── guifansrc/                        # 规范 PDF 源(不入库,见 .gitignore)
```

**技能安装机制**:仓库内 `tools/guifan-chaxun/` 不是 Codex 技能发现路径(发现范围:全局 `~/.Codex/skills/`、项目 `.Codex/skills/`、插件)。本机通过软链 `~/.Codex/skills/guifan-chaxun → tools/guifan-chaxun` 加载;**新机器克隆本仓库后需重建该软链**(或复制目录),否则技能不在技能列表里。

**数据布局**(`library_data/<源文件相对父目录>/<book_id>/`,目录结构与 guifansrc 一致:`gonglu/` 子目录的书在 `library_data/gonglu/<book_id>/`,库根目录书在 `library_data/<book_id>/`):`meta.json`(元数据+probe 证据+chapter_list,含 fmt/virtual/pages_dir/source_abs 字段)、`toc.md`(章节索引表,查询导航核心)、`clauses.idx`(条文号→页码 TSV,含 expl/ocr/低置信标记)、`chapters/chNN-*.md`(分章全文,头部注释含页码/条文号范围,正文每页前有 `【第 N 页】`)、`ocr/NNN.txt`(仅 OCR 书:扫描 PDF/图片)、`extracted/NNN.txt`(仅非 PDF 文本书:Word/Excel/OFD 提取文本,虚拟页或物理页)。

**book_id 规则**:`= 源文件名去扩展名`(如 `1.公路桥涵养护规范(JTG 5120-2021)`、`27.《城市桥梁设计规范》局部修订条文`),与 guifansrc 里的知识文件一一对应。**guifansrc 支持多层文件夹**:`file` 字段存相对 library_dir 的路径(`rglob` 递归收集,`status` 一致性检查用相对路径键避免同名混淆);同名不同路径时 book_id 加完整相对路径的稳定哈希后缀(父目录重名也不会碰撞)。**人工元数据优先**:`_index_one` 里若 bookshelf 已有同源文件条目,则 std_no/title/version/id 以书架为准(文件名没写编号的书,人工在 bookshelf.json 补 std_no 即可,如 6.公路隧道养护技术规范 的 std_no=JTG 5130—2026)。

**页模型**:PDF/OFD/图片书 = 物理页;Word/Excel/txt 等无物理页的文档按段落累计 ~500 字符切**虚拟页**(段落不撕裂,上限 400 页),meta 里 `virtual=true`,toc.md 表头"页"而非"PDF 页",`read` 输出带【虚拟页】标记。**read 分派**:`pages_dir=ocr` 读 ocr/NNN.txt、`pages_dir=extracted` 读 extracted/NNN.txt、缺省(PDF 文字书)现场 fitz 提取。**字段兼容**:meta/bookshelf 双写 source_abs/source_mtime 与旧 pdf_abs/pdf_mtime，并记录 `source_mtime_ns`+`source_size` 作精确增量判定；读取一律新字段优先、旧字段回退,重索引自然升级。

## 关键设计决策(改代码勿重蹈)

1. **文字 PDF 不落盘 pages/**(方案 A):提取在内存聚合,`read` 现场从 PDF 提取;OCR 书的 `ocr/` 必须保留(它是 OCR 原始产物,章文件/条文索引都从它生成)。**非 PDF 书相反,必须落盘 extracted/**(源文件重提取要走 COM 转换,慢且脆弱,`read` 查询时不可现场转换)。改 extract/load 逻辑时注意三者读源不同(fitz 现场 / ocr/ / extracted/)。
2. **质量检测三信号**(`probe_pdf`):无字页占比(扫描)、常用字覆盖率<0.95、标点污染率>0.08 且劣化页>60%(乱码)。GB 5768 系列有**两种乱码模式**(A:汉字可读但数字→符号、覆盖率 0.85-0.94;B:全乱、覆盖率 0),单信号抓不全,双信号+条文号命中仲裁缺一不可。封面/公告/目录页(前 5 页)只参与扫描判定,不参与覆盖率。
3. **TOC 三路径回退**:书签(存在 page=-1 即弃)→ 目录页解析(区段检测:带"目次/目录"标记+目录行密度;**正文页信号截断**;页码"- 1 -"残缺用章标题回正文定位+偏移校准)→ 正文扫描/条文号聚类。**OCR 书一律走"条文号聚类定页+顺序补章"**(`clause_cluster`),目录页解析结果不可信。
4. **条文说明三种排版**:独立末章(书后半部+页首"条文说明"+同页重新从第 1 章编号才判)、随条文内嵌(不建章)、无。clauses.idx 里条文说明区条目标 expl=1(clause 直查双命中)。
5. **OCR 数字混淆归一化**(`OCR_NORM_TABLE`):s/S→5、l/I/丨→1、O/o→0、$^→去符号。GB 5768.9-2025 等新版条文号**跨行排版**("4." 行 + 下一行 "5" = 4.5),`build_clauses` 有跨行组合(标 low 置信)。
6. **并发写 bookshelf 竞态**:`index --jobs N` 并行时 `_index_one` **不写 bookshelf.json**,`cmd_index` 在单线程合并结果再写;`_index_one` 返回 `(path, status, msg, entry)` 四元组。**COM 两阶段**:doc/xls/wps/et 老格式严格串行(COM apartment 模型,线程池内调用会挂起进程);`ComContext` 单例复用 Office/WPS Application,连续 2 次失败重建,退出时清理临时文件与残留 WPS 进程(差分 PID,不碰用户已打开的)。
7. **章文件后缀 .md**:`write_chapters` 清理时兼容 `*.txt`+`*.md`;grep/status 的 glob 同兼容。toc.md 里章文件引用同步。
8. **控制台/Windows**:路径含中文/全角括号必须引号;文件名首尾空格、全角破折号"—"是合法字符;`\xa0`/`\u3000` 是规范 PDF 的合法标题分隔符,正则字符类必须包含。
9. **常见正则**:条文号 `^\d{1,2}\.\d{1,2}(?:\.\d{1,3})?(?=空白|汉字)`(排除裸数字行列项);章标题兼容同行/粘连/独立数字行三种排版。

## 扩展约定

- **新书入库**:任意受支持格式文件放 `library_dir` → `spec.py index --all`(增量,mtime 未变自动跳过;OCR 书断点续跑)。文件名带序号前缀(`N.名称(编号).pdf`);zip 压缩包不解包不索引,需自行解包后放入。
- **新领域扩展**:常用字表可能覆盖不全 → `spec.py update-chars` 重新生成;`bookshelf.json` 补 category/alias/替代关系。
- **实战易漏项沉淀**:每次查询踩到漏项,追加到 `references/query_notes.md` 对应场景的"易漏项"小节;新场景按同格式新建小节(该文件是防漏机制,SKILL.md 工作流步骤 4 引用它)。
- **查询用法文档**:agent 使用姿势在 `SKILL.md`(两态工作流/输出格式/禁令),改 SKILL.md 时保持与 spec.py 实际行为一致。

## 用户协作规定

- **git 操作需明确指示**:未经用户明确指示(如"保存/提交/上传/推送"等字样),不得执行 git commit / push 等版本控制操作;只修改代码并汇报结果,提交与否等用户发话。
- 用户说"写进去/加个功能/改一下"时,默认只改文件、不动 git。
