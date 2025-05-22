import redis.asyncio as redis

# Singleton Redis connection
redis_client = redis.Redis(
    host="localhost",  # or your Docker host/IP
    port=6379,
    db=0,
    decode_responses=True  # If storing JSON/text
)
