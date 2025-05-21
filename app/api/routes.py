from fastapi import APIRouter, HTTPException
from app.core.parser import parse_requirements
from app.core.osv import check_osv_vulnerabilities
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


# 🔹 Request schema
class ApplicationInput(BaseModel):
    name: str
    description: Optional[str] = None
    requirements: str

# 🔹 Response schema
class DependencyVulnerability(BaseModel):
    name: str
    version: str
    vulnerabilities: List[dict]
    error: Optional[str] = None


class ApplicationResponse(BaseModel):
    application: str
    dependencies_checked: List[DependencyVulnerability]
    ignored_dependencies: List[str]


# 🔹 Route: Create application
@router.post("/applications/", response_model=ApplicationResponse)
async def create_application(app_data: ApplicationInput):
    valid_deps, ignored_deps = parse_requirements(app_data.requirements)

    results = []
    for name, version in valid_deps:
        result = check_osv_vulnerabilities(name, version)
        results.append(result)

    return {
        "application": app_data.name,
        "dependencies_checked": results,
        "ignored_dependencies": ignored_deps,
    }
