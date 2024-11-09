from datetime import datetime
from geopy.distance import geodesic

def format_time(time_str):
    """
    Format a time string into a datetime object.
    Args:
        time_str (str): Time in string format (e.g., '9:00 AM').
    Returns:
        datetime: Formatted datetime object.
    """
    return datetime.strptime(time_str, '%I:%M %p')

def calculate_distance(location1, location2):
    """
    Calculate the distance in kilometers between two locations.
    Args:
        location1 (tuple): (latitude, longitude) of the first location.
        location2 (tuple): (latitude, longitude) of the second location.
    Returns:
        float: Distance in kilometers.
    """
    return geodesic(location1, location2).kilometers

def parse_interests(interests_str):
    """
    Parse a comma-separated string of interests into a list.
    Args:
        interests_str (str): Comma-separated interests (e.g., 'culture, food, shopping').
    Returns:
        list: List of interest strings.
    """
    return [interest.strip() for interest in interests_str.split(',')]