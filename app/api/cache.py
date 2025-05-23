import json
from app.core.redis_client import redis_client

# Operations for cache.

def _make_cache_key(package: str, version: str) -> str:
    return f"osv:{package}:{version}"

async def get_cached_vulns(package: str, version: str):
    key = _make_cache_key(package, version)
    raw = await redis_client.get(key)
    return json.loads(raw) if raw else None

async def set_cached_vulns(package: str, version: str, data: dict, ttl: int = 3600):
    key = _make_cache_key(package, version)
    await redis_client.set(key, json.dumps(data), ex=ttl)
