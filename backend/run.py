import os
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

env = os.getenv("ENV", "prod")
reload = env == "dev"

logger.info(f"Starting server in {env.upper()} mode")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=reload
    )
