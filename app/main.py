import config
from fastapi import FastAPI
# Project imports
from .core import parser as psr
from .core import osv
from .api.routes import router

# Create FastAPI app
app = FastAPI(
    title=config.APP_NAME,
    version=config.VERSION
)

app.include_router(router)

if __name__ == "__main__":
    # Open the sample_requirements.txt file and read its content
    with open(config.TEST_DATA_PATH  + "/sample_requirements.txt") as f:
        requirements = f.read()


    valid, ignored = psr.parse_requirements(requirements)

    print("Valid dependencies:", valid)
    print("Ignored dependencies:", ignored)
