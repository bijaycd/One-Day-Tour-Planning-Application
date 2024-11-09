from src.tourplanner.llm.llm_interface import generate_response

def collect_user_preferences():
    """
    Collect user preferences for the day tour using the Ollama model for prompts.
    Returns a dictionary of preferences.
    """
    preferences = {}

    # Ask for the city
    city_prompt = "Which city would you like to explore?"
    preferences['city'] = generate_response(city_prompt).strip()

    # Ask for the start time
    start_time_prompt = "What time would you like to start your day? (e.g., 9:00 AM)"
    preferences['start_time'] = generate_response(start_time_prompt).strip()

    # Ask for the end time
    end_time_prompt = "What time would you like to end your day? (e.g., 6:00 PM)"
    preferences['end_time'] = generate_response(end_time_prompt).strip()

    # Ask for the budget
    budget_prompt = "What's your budget for the day?"
    preferences['budget'] = generate_response(budget_prompt).strip()

    # Ask for interests
    interests_prompt = "Please specify your interests (e.g., culture, food, shopping, adventure):"
    interests_response = generate_response(interests_prompt).strip()
    preferences['interests'] = [interest.strip() for interest in interests_response.split(',')]

    return preferences