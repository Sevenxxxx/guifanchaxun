# PDF 处理方法(处理规范 PDF 前必读)

本文档覆盖本 skill 处理规范 PDF 的全部工具与方法。跑 `spec.py index` 之前读完本文。

## 1. 工具优先级

| 场景 | 工具 | 说明 |
|---|---|---|
| 加书/建索引(唯一主工具) | `spec.py index` | 内部用 pymupdf 提取 + tesseract OCR,自动分流 |
| 查询(主路径) | Read/Grep 章节文件 | 纯文件系统操作,零 Python 依赖 |
| 按页复核(兜底) | `spec.py read` | 文字书现场从 PDF 提取(不落盘缓存);OCR 书读 ocr/NNN.txt |
| 条文号直查 | `spec.py clause` | 读 clauses.idx;未命中给相邻条文 |
| pdftotext | 仅文字书兜底 | **对坏 ToUnicode CMap 的"伪文字版"无效**(提取出的是乱码),此类书必须 OCR |
| tesseract OCR | 仅索引时整本一次性 | 查询路径永不 OCR |

## 2. 页范围提取与 token 预算

- 单次 `read` 最多 20 页;章节文件只读锁定的章,不整本加载。
- 索引产物落盘(`chapters/`、`ocr/NNN.txt`[仅 OCR 书]);**文字书不保留按页缓存**,`read` 按需现场从 PDF 提取。
- `grep` 默认最多 30 条命中,`--ctx` 控制上下文行数,防 token 爆炸。

## 3. OCR 分支

- 何时触发:索引时质量检测判定 `type=ocr`(纯扫描件、或文字层乱码的"伪文字版")。判定证据在 `meta.json` 的 `probe` 字段。
- 流程:300dpi 渲染每页 → tesseract(chi_sim,psm 3)stdin 管道 → 写入 `ocr/NNN.txt`;**断点续跑**(已存在页自动跳过),每 10 页打印进度。
- 精度注意:OCR 常把 `5` 识成 `s`、`1` 识成 `l`、句点识成 `$`——条文索引已做归一化匹配(s→5、l→1、$→去符号等),但仍可能有漏网;`clause` 未命中时用页内 grep 二次确认;章标题可能被误读(如"总则"→"总册"),以章号和页码为准。
- 失败页:重试 1 次仍失败记入 `meta.json.ocr.failed_pages` 并继续,不阻断索引。
- 重识别:`spec.py ocr <book> --force`;单页:`spec.py ocr <book> --start N --end N --force`。

## 4. 乱码识别(三信号)

判定靠**常用字覆盖率**与**标点污染率**双信号(两种乱码模式都覆盖):

- 覆盖率 < 0.95(汉字按 ~3500 常用字表计)→ 乱码;
- 标点污染率 > 0.08 且劣化页占比 > 60% → 乱码(汉字可读但数字变符号的模式,覆盖率正常也能抓住);
- 纯扫描件:全书提取字符 <20/页 占比 > 90%。

查询时若 `read` 输出 `[警告:部分页疑似乱码]`,该页**不可作为原文引用**,应 `spec.py ocr` 该页或如实告知用户。

## 5. Windows 注意事项

- 控制台 GBK:spec.py 内部已 `sys.stdout.reconfigure(utf-8)`,无需处理;自己写临时脚本时加 `PYTHONIOENCODING=utf-8`。
- 路径含中文/全角括号/空格:命令行参数必须加引号;支持通配符(如 `"*公路桥涵养护规范*.pdf"`)。
- Python 命令:`python`(3.12)。
- tesseract:装于 `C:\Program Files\Tesseract-OCR\`,语言包 chi_sim 已放 `<skill>/../guifan-chaxun-scripts/scripts/tessdata/`(config 里 `ocr_tessdata_dir` 指向,自包含可移植);验证:`"C:\Program Files\Tesseract-OCR\tesseract.exe" --list-langs`。
- 全角空格 U+3000 与不换行空格 U+00A0 是规范 PDF 的合法标题/目录分隔符,正则已兼容,勿当噪声剔除。

## 6. 规范 PDF 格式速查(索引器已适配,勿重踩)

- 条文号:GB 是 X.X 两层("5.2限制速度值…"),JTG 是 X.X.X 三层;有独立数字行与同行粘连两种排版;条下列项是裸数字行("1"/"2"),不是条文。
- 章标题:同行式("4 桥梁养护与维修")/粘连式("7二、三级…")/独立数字行(数字行+下一行标题)三种。
- 条文说明:JTG 老排版在书后半部独立成章(条文号与正文重复,索引已用 expl 标记区分);新排版(如 JTG 5130-2026 隧道规范)条文说明随条文内嵌,无独立章。
- 目录页:页码有"- 1 -"包横线、纯点线无页码、残缺等多种形态;目录页正文页码与 PDF 页码有偏移(索引时自动校准,`toc.md` 标注"正文页")。
- 伪文字版:GB 5768 系列等 ToUnicode CMap 损坏,提取中文全是乱码("犌犅５７６８"),pdftotext/pymupdf 均无效,只能 OCR。
