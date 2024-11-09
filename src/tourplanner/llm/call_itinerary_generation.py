from src.tourplanner.llm.llm_interface import generate_response

def suggest_itinerary(city, interests):
    """
    Generate a suggested itinerary based on city and interests.
    Args:
        city (str): The city name.
        interests (list): List of user interests.
    """
    prompt = f"Please create an itinerary for a one-day tour in {city} that includes {', '.join(interests)}."
    return generate_response(prompt)