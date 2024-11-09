import streamlit as st
from src.tourplanner.frontend.chat_interface import main as chat_main
from src.tourplanner.frontend.itinerary_display import main as itinerary_main
from src.tourplanner.frontend.login import main as login_main

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Login", "Plan Your Tour", "View Optimized Itinerary"))

    if page == "Login":
        login_main()
    elif page == "Plan Your Tour":
        chat_main()
    elif page == "View Optimized Itinerary":
        itinerary_main()

if __name__ == "__main__":
    main()