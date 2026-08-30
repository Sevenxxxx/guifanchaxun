@echo off
rem DSH CLI launcher: cd into the checkout, then forward all args.
rem Keep checkout path in sync with DSH_CHECKOUT in webapp\config.py.
cd /d "C:\Users\Seven\Desktop\deepseek-harness"
node apps\cli\lib\bin.js %*
