"""入口:python -m webapp(在仓库根目录执行)。"""
import uvicorn

from webapp import config

if __name__ == "__main__":
    uvicorn.run("webapp.main:app", host=config.HOST, port=config.PORT, log_level="info")
