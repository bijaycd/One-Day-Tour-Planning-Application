from fastapi import APIRouter
from src.tourplanner.agents.optimization_agent import optimize_itinerary

router = APIRouter()

@router.post("/optimize")
def optimize(itinerary: list, budget: float, travel_costs: dict):
    """
    Endpoint to optimize the itinerary.
    """
    optimized_itinerary = optimize_itinerary(itinerary, budget, travel_costs)
    return {"optimized_itinerary": optimized_itinerary}