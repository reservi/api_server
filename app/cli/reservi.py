import uvicorn
from sqlalchemy import create_engine

def main() -> None:
    config = uvicorn.Config("app.app:api", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()