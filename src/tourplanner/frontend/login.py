import streamlit as st

def login_screen():
    """
    Displays a simple login screen.
    """
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # For simplicity, we're just setting a session state variable
        st.session_state.logged_in = True
        st.success(f"Welcome, {username}!")

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.write("You are logged in!")
    else:
        login_screen()

if __name__ == "__main__":
    main()