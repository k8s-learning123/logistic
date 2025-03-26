from fastapi import APIRouter

from src.cache_client import cache_client

router = APIRouter()

@router.get("/")
async def main():
    cache_client.set("name", "example", 300)
    return {
        "message": await cache_client.get("name")
    }