import streamlit as st

# Check if "current_page" is in session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

def display_home():
    st.header("Home Page")
    st.write("Welcome to the Home Page.")
    if st.button("Go to Page 1"):
        st.session_state.current_page = "Page1"

def display_page1():
    st.header("Page 1")
    st.write("Welcome to Page 1.")
    if st.button("Go back to Home"):
        st.session_state.current_page = "Home"
    
st.markdown("""
    <a href="http://172.31.28.68:3000/login" target="_blank">Login Page</a>
""", unsafe_allow_html=True)


st.markdown("""
    <a href="http://172.31.28.68:3000/logout" target="_blank">Logout Page</a>
""", unsafe_allow_html=True)

# st.markdown("""
#     <a href="http://localhost:3000" target="_blank">Login Page</a>
# """, unsafe_allow_html=True)

# Page routing
if st.session_state.current_page == "Home":
    display_home()
elif st.session_state.current_page == "Page1":
    display_page1()