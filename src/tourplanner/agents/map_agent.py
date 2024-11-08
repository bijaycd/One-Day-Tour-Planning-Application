import requests

def generate_map(city, itinerary):
    """
    Generate a map for the itinerary with marked locations.
    Args:
        city (str): City name.
        itinerary (list): List of itinerary stops.
    
    Returns:
        URL link to the map or map image.
    """
    # Placeholder for a real mapping API
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={city}&zoom=13&size=600x400"
    
    # Add each location to the map URL as markers
    for stop in itinerary:
        map_url += f"&markers=color:red%7Clabel:{stop['name']}%7C{stop['name']}"
    
    return map_url