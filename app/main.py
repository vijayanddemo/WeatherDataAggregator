# app/main.py
from fastapi import FastAPI, HTTPException
import httpx
 
app = FastAPI(title="Weather Data Aggregator")
 
# Example external APIs (replace with your own keys)
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_KEY = "YOUR_OPENWEATHER_API_KEY"
 
WEATHERAPI_URL = "http://api.weatherapi.com/v1/current.json"
WEATHERAPI_KEY = "YOUR_WEATHERAPI_KEY"
 
 
async def fetch_openweather(city: str):
    async with httpx.AsyncClient() as client:
        params = {"q": city, "appid": OPENWEATHER_KEY, "units": "metric"}
        resp = await client.get(OPENWEATHER_URL, params=params)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail="OpenWeather API error")
        data = resp.json()
        return {
            "source": "OpenWeather",
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
        }
 
 
async def fetch_weatherapi(city: str):
    async with httpx.AsyncClient() as client:
        params = {"key": WEATHERAPI_KEY, "q": city}
        resp = await client.get(WEATHERAPI_URL, params=params)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail="WeatherAPI error")
        data = resp.json()
        return {
            "source": "WeatherAPI",
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
        }
 
 
@app.get("/weather/{city}")
async def get_weather(city: str):
    """Fetch weather from multiple sources and aggregate results"""
    openweather = await fetch_openweather(city)
    weatherapi = await fetch_weatherapi(city)
 
    return {
        "city": city,
        "results": [openweather, weatherapi],
        "average_temp": round((openweather["temperature"] + weatherapi["temperature"]) / 2, 2),
    }