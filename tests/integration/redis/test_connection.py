import pytest

from src.cache_client import cache_client

@pytest.mark.asyncio
async def test_connection():
    assert (await cache_client.ping()) == True 