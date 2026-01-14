import pytest
from httpx import AsyncClient
from app.main import app
 
@pytest.mark.asyncio
async def test_weather_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/weather/London")
    assert response.status_code == 200
    data = response.json()
    assert "city" in data
    assert "sources" in data
    assert "average_temp" in data