# Start script: bind 0.0.0.0 so other PCs / public IP / Tailscale can access.
# Compatible with Task Scheduler autostart: switch to the repo root first
# (python -m webapp requires it). Prereq: firewall 8090 opened.
$scriptPath = $MyInvocation.MyCommand.Path
$repo = Split-Path -Parent (Split-Path -Parent $scriptPath)  # parent of webapp = repo root
Set-Location $repo
$env:PYTHONIOENCODING = 'utf-8'
$env:GFC_HOST = '0.0.0.0'
# Concurrency cap defaults to 5 (config.py GFC_MAX_CONCURRENT). Override here if needed:
# $env:GFC_MAX_CONCURRENT = '3'
python -m webapp
