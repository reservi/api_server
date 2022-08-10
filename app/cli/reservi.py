import uvicorn

def main() -> None:
    config = uvicorn.Config("app.app:api", port=5000, log_level="debug", root_path="/api/")
    server = uvicorn.Server(config)
    server.run()