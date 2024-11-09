from src.tourplanner.llm.llm_interface import generate_response

def recall_user_preferences(user_preferences):
    """
    Generate a summary of the user’s preferences.
    Args:
        user_preferences (dict): User preferences retrieved from memory.
    """
    preferences_text = ", ".join(f"{key}: {value}" for key, value in user_preferences.items())
    prompt = f"Based on the user’s previous preferences: {preferences_text}, provide a summary."
    return generate_response(prompt)