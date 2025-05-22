from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.core.parser import parse_requirements
from app.core.osv import check_osv_vulnerabilities
from pydantic import BaseModel
from typing import List, Optional
import asyncio

router = APIRouter()

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


@router.post("/applications/", response_model=ApplicationResponse)
async def create_application(
    name: str = Form(...),
    description: Optional[str] = Form(None),
    requirements_file: UploadFile = File(...)
):
    if not requirements_file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are accepted")

    content = await requirements_file.read()
    requirements = content.decode()

    valid_deps, ignored_deps = parse_requirements(requirements)

    # Run OSV checks concurrently
    tasks = [
        check_osv_vulnerabilities(dep_name, dep_version)
        for dep_name, dep_version in valid_deps
    ]
    results_raw = await asyncio.gather(*tasks)
    results = [DependencyVulnerability(**r) for r in results_raw]

    return ApplicationResponse(
        application=name,
        dependencies_checked=results,
        ignored_dependencies=ignored_deps
    )
