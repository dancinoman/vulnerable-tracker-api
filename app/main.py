import config
from fastapi import FastAPI

# Project imports
from .api.routes import router

# Create FastAPI app
app = FastAPI(
    title=config.APP_NAME,
    version=config.VERSION
)

app.include_router(router)
