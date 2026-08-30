# One-time setup: isolated DSH home + sdk profile materialization + credential copy.
# Usage (repo root): powershell -ExecutionPolicy Bypass -File webapp\setup.ps1
$ErrorActionPreference = 'Stop'

$webapp = Split-Path -Parent $MyInvocation.MyCommand.Path
$dshHome = Join-Path $webapp 'dsh-home'
New-Item -ItemType Directory -Force -Path $dshHome | Out-Null

# 1) copy local DSH credentials (same DeepSeek key as the GUI; local file copy only)
$src = Join-Path $env:USERPROFILE '.dsh\.credentials.yaml'
if (-not (Test-Path $src)) {
    throw "credentials not found: $src (configure the model in DSH GUI first)"
}
Copy-Item $src (Join-Path $dshHome '.credentials.yaml') -Force

# 2) materialize sdk profile (built-in template dsh-base + dsh-sdk-app; offline mirror)
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
