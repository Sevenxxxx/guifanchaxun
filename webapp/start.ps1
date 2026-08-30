# 局域网/Tailscale 访问启动脚本:绑定 0.0.0.0,其他电脑浏览器可直接访问
#   Tailscale:   http://100.85.0.30:8090
#   局域网 WLAN: http://192.168.1.9:8090
# 前置:已放行防火墙 8090(见 README"局域网/Tailscale 访问"一节)
$env:PYTHONIOENCODING = 'utf-8'
$env:GFC_HOST = '0.0.0.0'
python -m webapp
