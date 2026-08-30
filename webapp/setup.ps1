# 涓€娆℃€у垵濮嬪寲:POC 鐙珛 DSH home + sdk profile 鏉愯川鍖?+ 鍑嵁澶嶅埗
# 鐢ㄦ硶(鍦ㄤ粨搴撴牴): powershell -ExecutionPolicy Bypass -File webapp\setup.ps1
$ErrorActionPreference = 'Stop'

$webapp = Split-Path -Parent $MyInvocation.MyCommand.Path
$dshHome = Join-Path $webapp 'dsh-home'

New-Item -ItemType Directory -Force -Path $dshHome | Out-Null

# 1) 澶嶅埗鏈満 DSH 鍑嵁(涓?GUI 鍚屼竴浠?DeepSeek 瀵嗛挜;浠呮湰鏈烘枃浠跺鍒?涓嶅浼?
$src = Join-Path $env:USERPROFILE '.dsh\.credentials.yaml'
if (-not (Test-Path $src)) {
    throw "鏈壘鍒板嚟鎹枃浠? $src(璇峰厛鍦ㄦ湰鏈?DSH GUI 涓厤缃繃妯″瀷)"
}
Copy-Item $src (Join-Path $dshHome '.credentials.yaml') -Force

# 2) 鏉愯川鍖?sdk profile(鍐呯疆妯℃澘 dsh-base + dsh-sdk-app;闀滃儚 checkout 渚濊禆闂寘,绂荤嚎瀹屾垚)
$env:DSH_HOME = $dshHome
$launcher = Join-Path $webapp 'dsh_launcher.cmd'
$dump = Join-Path $webapp 'dump-default-config.txt'
& $launcher --profile sdk --dump-default-config *> $dump
if ($LASTEXITCODE -ne 0) {
    Get-Content $dump -ErrorAction SilentlyContinue
    throw "sdk profile 鍒濆鍖栧け璐?exit $LASTEXITCODE),璇﹁ $dump"
}

$skillRows = (Select-String -Path $dump -Pattern 'dsh-skill' -SimpleMatch | Measure-Object).Count
Write-Host "OK: DSH_HOME = $dshHome"
Write-Host "     sdk profile 宸叉潗璐ㄥ寲;缁勫悎杈撳嚭: $dump(skill 鐩稿叧琛?$skillRows 鏉?"
