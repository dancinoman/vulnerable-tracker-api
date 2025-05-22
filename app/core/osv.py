import httpx

OSV_API_URL = "https://api.osv.dev/v1/query"

async def check_osv_vulnerabilities(package_name: str, version: str) -> dict:
    payload = {
        "package": {"name": package_name, "ecosystem": "PyPI"},
        "version": version
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(OSV_API_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            return {
                "name": package_name,
                "version": version,
                "vulnerabilities": data.get("vulns", [])
            }
    except Exception as e:
        return {
            "name": package_name,
            "version": version,
            "vulnerabilities": [],
            "error": str(e)
        }
