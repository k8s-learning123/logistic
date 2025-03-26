import aioredis

from src.conf import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

cache_client = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", password=REDIS_PASSWORD, db=0)