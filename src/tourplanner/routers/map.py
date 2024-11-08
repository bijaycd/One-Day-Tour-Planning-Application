from fastapi import APIRouter
from src.tourplanner.agents.map_agent import generate_map

router = APIRouter()

@router.get("/map")
def create_map(city: str, itinerary: list):
    """
    Endpoint to generate a map for the itinerary.
    """
    map_url = generate_map(city, itinerary)
    return {"map_url": map_url}