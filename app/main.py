import config
from fastapi import FastAPI

# Project imports
from .api.routes import router
from app.core.redis_client import redis_client

async def lifespan(app: FastAPI):
    yield
    await redis_client.aclose()

# Create FastAPI app
app = FastAPI(
    title=config.APP_NAME,
    version=config.VERSION,
    lifespan=lifespan,
)

app.include_router(router)
