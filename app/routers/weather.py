from fastapi import APIRouter, HTTPException
from app.services.weather_service import fetch_openweather, fetch_weatherapi
from app.models.weather_models import WeatherResponse
 
router = APIRouter(prefix="/weather", tags=["Weather"])
 
@router.get("/{city}", response_model=WeatherResponse)
async def get_weather(city: str):
    try:
        openweather = await fetch_openweather(city)
        weatherapi = await fetch_weatherapi(city)
 
        avg_temp = round((openweather.temperature + weatherapi.temperature) / 2, 2)
 
        return WeatherResponse(
            city=city,
            sources=[openweather, weatherapi],
            average_temp=avg_temp
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))