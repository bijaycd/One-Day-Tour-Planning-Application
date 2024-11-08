from fastapi import APIRouter
from src.tourplanner.agents.user_interaction_agent import collect_user_preferences

router = APIRouter()

@router.get("/preferences")
def get_user_preferences():
    """
    Endpoint to collect user preferences.
    """
    return {"preferences": collect_user_preferences()}