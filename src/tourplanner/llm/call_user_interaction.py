from src.tourplanner.llm.llm_interface import generate_response

def ask_for_city():
    """
    Prompt the LLM to ask the user for the city they wish to visit.
    """
    prompt = "Please tell me the city you would like to explore today."
    return generate_response(prompt)

def ask_for_interests():
    """
    Prompt the LLM to ask the user for their interests.
    """
    prompt = "What are your interests? Examples: culture, food, shopping, adventure."
    return generate_response(prompt)