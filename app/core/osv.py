import httpx
from app.api.cache import get_cached_vulns, set_cached_vulns

OSV_API_URL = "https://api.osv.dev/v1/query"

async def check_osv_vulnerabilities(package_name: str, version: str) -> dict:
    """
    Prioritize cache to optimize performance.
    If there is no cache then a request is sent
    Returns a dict of vulnerability data
    """
    # Attempt to get cache first
    cached = await get_cached_vulns(package_name, version)
    if cached:
        return cached

    payload = {
        "package": {"name": package_name, "ecosystem": "PyPI"},
        "version": version
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(OSV_API_URL, json=payload)
            response.raise_for_status()
            data = {
                "name": package_name,
                "version": version,
                "vulnerabilities": response.json().get("vulns", [])
            }

            # Cache result
            await set_cached_vulns(package_name, version, data)
            return data

    except Exception as e:
        return {
            "name": package_name,
            "version": version,
            "vulnerabilities": [],
            "error": str(e)
        }
