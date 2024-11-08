from fastapi import APIRouter
from src.tourplanner.agents.memory_agent import save_user_preferences, get_user_preferences

router = APIRouter()

@router.post("/memory/save")
def save_preferences(user_id: str, preferences: dict):
    """
    Endpoint to save user preferences.
    """
    save_user_preferences(user_id, preferences)
    return {"message": "Preferences saved successfully"}

@router.get("/memory/{user_id}")
def retrieve_preferences(user_id: str):
    """
    Endpoint to retrieve user preferences.
    """
    preferences = get_user_preferences(user_id)
    return {"preferences": preferences}