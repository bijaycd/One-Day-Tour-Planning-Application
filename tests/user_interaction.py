import sys
import os

# Adjust the path below to your project's root directory
project_root = os.path.abspath("..")  # Go one level up, assuming Jupyter is in 'src/tourplanner' folder
sys.path.append(project_root)
from src.tourplanner.agents.user_interaction_agent import collect_user_preferences

def test_collect_user_preferences():
    """
    Test the collect_user_preferences function with the Ollama integration.
    """
    # Run the function and collect preferences
    preferences = collect_user_preferences()

    # Check if preferences is a dictionary
    assert isinstance(preferences, dict), "Preferences should be a dictionary"

    # Check if all expected keys are present
    expected_keys = ['city', 'start_time', 'end_time', 'budget', 'interests']
    for key in expected_keys:
        assert key in preferences, f"Missing key in preferences: {key}"

    # Check if interests is a list
    assert isinstance(preferences['interests'], list), "Interests should be a list"

    # Print the collected preferences for review
    print("Collected Preferences:", preferences)

# Run the test function
if __name__ == "__main__":
    test_collect_user_preferences()