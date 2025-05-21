import os
from fastapi import FastAPI

# Project imports
from .core import parser as psr
from .core import osv
from .api.routes import router

# Paths of projects
CURENT_PATH = project_root = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURENT_PATH)
TEST_DATA_PATH = file_path = os.path.join(PROJECT_ROOT,"tests", "data")

# Create FastAPI app
app = FastAPI(
    title="Python Vulnerability Tracker",
    version="1.0.0"
)

app.include_router(router, prefix="/api")
# Open the sample_requirements.txt file and read its content
with open(TEST_DATA_PATH  + "/sample_requirements.txt") as f:
    requirements = f.read()


@router.post("/applications/")
async def create_application(app_data: dict):
    requirements = app_data.get("requirements", "")
    valid_deps, ignored_deps = psr.parse_requirements(requirements)

    results = []
    for name, version in valid_deps:
        # Check for vulnerabilities using the OSV API
        result = osv.check_osv_vulnerabilities(name, version)
        results.append(result)

    return {
        "application": app_data["name"],
        "dependencies_checked": results,
        "ignored_dependencies": ignored_deps
    }
