from fastapi import FastAPI
from app.routers import weather
 
app = FastAPI(title="Weather Data Aggregator")
 
# Register routers
app.include_router(weather. Router)