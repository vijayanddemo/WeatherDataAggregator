from pydantic import BaseModel
from typing import List
 
class WeatherSource(BaseModel):
    source: str
    temperature: float
    condition: str
 
class WeatherResponse(BaseModel):
    city: str
    sources: List[WeatherSource]
    average_temp: float