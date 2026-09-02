@echo off
rem DSH CLI launcher: cd into the checkout, then forward all args.
rem 优先用 GFC_DSH_CHECKOUT 环境变量(服务器设它,git pull 不影响);否则回退本机路径,与 config.py 保持一致。
if not defined GFC_DSH_CHECKOUT set "GFC_DSH_CHECKOUT=C:\Users\Seven\Desktop\deepseek-harness"
cd /d "%GFC_DSH_CHECKOUT%"
node apps\cli\lib\bin.js %*
