from fastapi import APIRouter
from src.tourplanner.agents.itinerary_generation_agent import generate_initial_itinerary

router = APIRouter()

@router.post("/itinerary")
def create_itinerary(city: str, start_time: str, end_time: str, interests: list):
    """
    Endpoint to generate an initial itinerary.
    """
    itinerary = generate_initial_itinerary(city, start_time, end_time, interests)
    return {"itinerary": itinerary}