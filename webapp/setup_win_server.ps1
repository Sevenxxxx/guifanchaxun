# Windows Server one-time setup: isolated DSH home + sdk profile materialization.
# Unlike setup.ps1, NO credential file copy: the server uses the DEEPSEEK_API_KEY
# environment variable (set it yourself).
# Prereqs (see deploy-win-server.md): config.py paths + dsh_launcher.cmd point to server locations.
# Usage (admin PowerShell, on the server): powershell -ExecutionPolicy Bypass -File webapp\setup_win_server.ps1
$ErrorActionPreference = 'Stop'

$webapp = Split-Path -Parent $MyInvocation.MyCommand.Path
$dshHome = Join-Path $webapp 'dsh-home'
New-Item -ItemType Directory -Force -Path $dshHome | Out-Null

# Credentials: no file copy. The llm adapter falls back to the DEEPSEEK_API_KEY env var
# (first question fails with MISSING_CREDENTIAL if it is not set).
if (-not ($env:DEEPSEEK_API_KEY)) {
    Write-Host "WARN: DEEPSEEK_API_KEY env var not detected (set Machine-level env var, then restart the shell)"
}

# Materialize the sdk profile (built-in template dsh-base + dsh-sdk-app; offline mirror).
$env:DSH_HOME = $dshHome
$launcher = Join-Path $webapp 'dsh_launcher.cmd'
$dump = Join-Path $webapp 'dump-default-config.txt'
& $launcher --profile sdk --dump-default-config *> $dump
if ($LASTEXITCODE -ne 0) {
    Get-Content $dump -ErrorAction SilentlyContinue
    throw "sdk profile init failed (exit $LASTEXITCODE); see $dump"
}

$skillRows = (Select-String -Path $dump -Pattern 'dsh-skill' -SimpleMatch | Measure-Object).Count
Write-Host "OK: DSH_HOME = $dshHome"
Write-Host "    sdk profile materialized; composition dump: $dump (skill rows: $skillRows)"
Write-Host "NEXT: set DEEPSEEK_API_KEY -> open firewall 8090 -> start via start.ps1"
