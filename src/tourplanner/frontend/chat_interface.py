import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"  # Base URL for the FastAPI backend

def get_user_preferences():
    """
    Collects user input for preferences and sends it to the backend.
    """
    st.header("One-Day Tour Planner")

    city = st.text_input("City to visit:")
    start_time = st.text_input("Start time (e.g., 9:00 AM):")
    end_time = st.text_input("End time (e.g., 6:00 PM):")
    budget = st.number_input("Budget for the day:", min_value=0)
    interests = st.text_area("Interests (e.g., culture, food, shopping):").split(',')

    if st.button("Generate Itinerary"):
        preferences = {
            "city": city,
            "start_time": start_time,
            "end_time": end_time,
            "budget": budget,
            "interests": interests
        }
        response = requests.post(f"{API_BASE_URL}/itinerary", json=preferences)
        
        if response.status_code == 200:
            itinerary = response.json().get("itinerary")
            st.session_state.itinerary = itinerary
            st.success("Itinerary generated successfully!")
        else:
            st.error("Failed to generate itinerary. Please try again.")

# Main function to run the Streamlit app
def main():
    st.title("Tour Planning Assistant")
    if "itinerary" not in st.session_state:
        st.session_state.itinerary = []

    get_user_preferences()

    # Display the itinerary if generated
    if st.session_state.itinerary:
        st.subheader("Generated Itinerary")
        for stop in st.session_state.itinerary:
            st.write(f"- **{stop['name']}** at {stop['time']}: {stop['description']}")

if __name__ == "__main__":
    main()