from datetime import datetime, timedelta
from src.tourplanner.database.data_access import get_attractions

def generate_initial_itinerary(city, start_time, end_time, interests):
    """
    Generate an initial itinerary based on user preferences.
    Args:
        city (str): The city to explore.
        start_time (str): Starting time of the tour.
        end_time (str): Ending time of the tour.
        interests (list): List of user interests.
    
    Returns:
        List of dictionaries representing the itinerary.
    """
    # Get a list of popular attractions from the database based on the city and interests
    attractions = get_attractions(city)
    itinerary = []

    # Convert start and end times to datetime objects for scheduling
    current_time = datetime.strptime(start_time, '%I:%M %p')
    end_time = datetime.strptime(end_time, '%I:%M %p')

    for attraction in attractions:
        if current_time >= end_time:
            break
        
        # Check if the attraction matches user interests
        if any(interest.strip().lower() in attraction['type'].lower() for interest in interests):
            itinerary.append({
                'name': attraction['name'],
                'description': attraction['description'],
                'time': current_time.strftime('%I:%M %p'),
                'type': attraction['type']
            })
            # Assume each attraction visit takes 1 hour, adjust as needed
            current_time += timedelta(hours=1)

    return itinerary