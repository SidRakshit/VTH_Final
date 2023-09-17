import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="MA"
)

st.header("Welcome to Stonks!")

st.title("Home Page")
st.sidebar.success("Select a page above.")

st.markdown("""
    <a href="http://172.31.28.68:3000/login" target="_blank">Login Page</a>
""", unsafe_allow_html=True)


st.markdown("""
    <a href="http://172.31.28.68:3000/logout" target="_blank">Logout Page</a>
""", unsafe_allow_html=True)

# st.header("Home Page")

with st.container():
    st.image("images/stonks_meme.jpg")

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
