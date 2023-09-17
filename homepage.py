import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="MA"
)

st.header("Welcome to Stonks!")

st.title("Main Page")
st.sidebar.success("Select a page above.")

st.markdown("""
    <a href="http://172.31.28.68:3000/login" target="_blank">Login Page</a>
""", unsafe_allow_html=True)


st.markdown("""
    <a href="http://172.31.28.68:3000/logout" target="_blank">Logout Page</a>
""", unsafe_allow_html=True)


# Check if "current_page" is in session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

def display_home():
    st.header("Home Page")
    with st.container():
        st.write(
                """We have created a stock simulator to provide people an experience of how the \
                    market works without the risk of losing real money.
                    Our platform is the perfect introduction intot he world of finance and will \
                        be an invaluable tool in the hands of finance clubs in an academic setting.
                """
                )
        st.write(
            """
            Login below or and then get started into the world of finance!
                """
        )
    # if st.button("Go to Page 1"):
    #     st.session_state.current_page = "Page 1"
    

def display_page1():
    st.header("INTERMEDIARY PAGE")
    st.write("Welcome to Page 1.")
    if st.button("Buy or Sell"):
        st.session_state.current_page = "Buy_Sell"
    if st.button("Portfolio"):
        st.session_state.current_page = "Portfolio"
def display_buy_sell():
    st.header("BUY OR SELL")
    st.write("Welcome to Buy and Sell")
    if st.button("Home"):
        st.session_state.current_page = "Home"
    if st.button("Back"):
        st.session_state.current_page = "Page 1" 

def display_portfolio():
    st.header("PORTFOLIO")
    st.write("Welcome to Portfolio")
    if st.button("Home"):
        st.session_state.current_page = "Home"
    if st.button("Back"):
        st.session_state.current_page = "Page 1"


# Page routing
if st.session_state.current_page == "Home":
    display_home()
elif st.session_state.current_page == "Page 1":
    display_page1()
elif st.session_state.current_page == "Buy_Sell":
    display_buy_sell()
elif st.session_state.current_page == "Portfolio":
    display_portfolio()