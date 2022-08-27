import pytest

from battleship.api.api import health_check


@pytest.mark.asyncio
async def test_health_api_returns_ok():
    assert await health_check() == {"msg": "OK"}
