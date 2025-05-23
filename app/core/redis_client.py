import redis.asyncio as redis

# Settings for Redis connection.
redis_client = redis.Redis(
    host="localhost",  
    port=6379,
    db=0,
    decode_responses=True 
)
