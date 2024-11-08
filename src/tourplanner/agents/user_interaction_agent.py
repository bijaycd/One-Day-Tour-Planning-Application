def collect_user_preferences():
    """
    Collect user preferences for the day tour.
    Returns a dictionary of preferences.
    """
    preferences = {}

    preferences['city'] = input("Which city would you like to explore? ")
    preferences['start_time'] = input("What time would you like to start your day? (e.g., 9:00 AM) ")
    preferences['end_time'] = input("What time would you like to end your day? (e.g., 6:00 PM) ")
    preferences['budget'] = input("What's your budget for the day? ")
    preferences['interests'] = input("Please specify your interests (e.g., culture, food, shopping, adventure): ").split(',')

    return preferences