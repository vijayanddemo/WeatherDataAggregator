import httpx
from app.models.weather_models import WeatherSource
 
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_KEY = "YOUR_OPENWEATHER_API_KEY"
 
WEATHERAPI_URL = "http://api.weatherapi.com/v1/current.json"
WEATHERAPI_KEY = "YOUR_WEATHERAPI_KEY"
 
async def fetch_openweather(city: str) -> WeatherSource:
    async with httpx.AsyncClient() as client:
        params = {"q": city, "appid": OPENWEATHER_KEY, "units": "metric"}
        resp = await client.get(OPENWEATHER_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        return WeatherSource(
            source="OpenWeather",
            temperature=data["main"]["temp"],
            condition=data["weather"][0]["description"]
        )
 
async def fetch_weatherapi(city: str) -> WeatherSource:
    async with httpx.AsyncClient() as client:
        params = {"key": WEATHERAPI_KEY, "q": city}
        resp = await client.get(WEATHERAPI_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        return WeatherSource(
            source="WeatherAPI",
            temperature=data["current"]["temp_c"],
            condition=data["current"]["condition"]["text"]
        )