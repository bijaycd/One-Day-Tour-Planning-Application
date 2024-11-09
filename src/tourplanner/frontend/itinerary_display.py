import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

def display_optimized_itinerary():
    """
    Display the optimized itinerary and allow further modifications.
    """
    st.header("Optimized Itinerary")

    if "optimized_itinerary" not in st.session_state:
        st.write("No itinerary generated yet.")
        return

    itinerary = st.session_state.optimized_itinerary

    for leg in itinerary:
        st.write(f"- From **{leg['from']}** to **{leg['to']}** by {leg['mode']} at {leg['time']}")
        st.write(f"  - Cost: ${leg['cost']:.2f}")
    
    if st.button("Finish Planning"):
        st.write("Itinerary planning complete. Have a great day!")

# Main function to run the display component
def main():
    st.title("Tour Planner - Optimized Itinerary")
    display_optimized_itinerary()

if __name__ == "__main__":
    main()