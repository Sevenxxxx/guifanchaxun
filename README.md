# 规范查询（guifan-chaxun）

面向中国工程规范及库内公文、通知、表格等资料的本地索引 skill。查询时按“书架 → 目录 → 章节 → 原文”逐级定位，不依赖向量数据库。

## 初始化（Windows）

1. 安装 Python 3.12，并确认 `python --version` 可用。
2. 在项目根目录执行 `python -m pip install -r requirements.txt`。
3. 安装 Tesseract 5，并在 `tools/guifan-chaxun-scripts/config.json` 中确认其路径；项目自带 `chi_sim` 语言包目录。
4. 把原始资料放入 `guifansrc/`，然后执行：

   ```powershell
   python tools/guifan-chaxun-scripts/scripts/spec.py index --all
   python tools/guifan-chaxun-scripts/scripts/spec.py status
   ```

旧版 Office/WPS 文件还需要已安装的 Office 或 WPS；Git 提交审查钩子需要 Git for Windows 提供的 `bash`。

## 常用操作

```powershell
# 检查新增、缺失和内容已变更的源文件
python tools/guifan-chaxun-scripts/scripts/spec.py status

# 增量重建；修改过的 OCR 源会自动重新 OCR
python tools/guifan-chaxun-scripts/scripts/spec.py index --all --jobs 4

# 查询
python tools/guifan-chaxun-scripts/scripts/spec.py list -q "桥梁"
python tools/guifan-chaxun-scripts/scripts/spec.py clause "书名或规范号" 4.2.1
```

## 验证

```powershell
python -m unittest discover -s tests -v
```

测试覆盖索引 ID 唯一性、源文件变更检测、原子写入和替代关系校验。完整工作流和数据格式见 [AGENTS.md](AGENTS.md) 与 `tools/guifan-chaxun/SKILL.md`。
