from fastapi import APIRouter
from src.tourplanner.agents.weather_agent import get_weather

router = APIRouter()

@router.get("/weather")
def fetch_weather(city: str):
    """
    Endpoint to fetch the weather for the given city.
    """
    weather_data = get_weather(city)
    return {"weather": weather_data}