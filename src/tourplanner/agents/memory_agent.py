from src.tourplanner.database.memory_manager import store_user_preference, retrieve_user_preferences

def save_user_preferences(user_id, preferences):
    """
    Save user preferences to the database.
    Args:
        user_id (str): Unique identifier for the user.
        preferences (dict): Dictionary of user preferences.
    """
    for preference_type, preference_value in preferences.items():
        store_user_preference(user_id, preference_type, preference_value)

def get_user_preferences(user_id):
    return retrieve_user_preferences(user_id)