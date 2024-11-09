from src.tourplanner.llm.llm_interface import generate_response
from src.tourplanner.utils.helpers import format_time, parse_interests
from src.tourplanner.utils.constants import DEFAULT_BUDGET
from src.tourplanner.utils.logger import log_info, log_error

def collect_user_preferences():
    """
    Collect user preferences for the day tour using the Ollama model for prompts.
    Returns a dictionary of preferences.
    """
    preferences = {}

    try:
        # Ask for the city
        city_prompt = "Which city would you like to explore?"
        preferences['city'] = generate_response(city_prompt).strip()
        log_info(f"User selected city: {preferences['city']}")

        # Ask for the start time
        start_time_prompt = "What time would you like to start your day? (e.g., 9:00 AM)"
        start_time_response = generate_response(start_time_prompt).strip()
        preferences['start_time'] = format_time(start_time_response)  # Format the time input
        log_info(f"User selected start time: {preferences['start_time']}")

        # Ask for the end time
        end_time_prompt = "What time would you like to end your day? (e.g., 6:00 PM)"
        end_time_response = generate_response(end_time_prompt).strip()
        preferences['end_time'] = format_time(end_time_response)  # Format the time input
        log_info(f"User selected end time: {preferences['end_time']}")

        # Ask for the budget
        budget_prompt = "What's your budget for the day?"
        budget_response = generate_response(budget_prompt).strip()
        preferences['budget'] = budget_response if budget_response else DEFAULT_BUDGET
        log_info(f"User budget: {preferences['budget']}")

        # Ask for interests
        interests_prompt = "Please specify your interests (e.g., culture, food, shopping, adventure):"
        interests_response = generate_response(interests_prompt).strip()
        preferences['interests'] = parse_interests(interests_response)  # Parse the interests input
        log_info(f"User interests: {preferences['interests']}")

    except Exception as e:
        log_error(f"Error collecting user preferences: {e}")

    return preferences