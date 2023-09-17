import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tade:", layout="wide")

with st.container():
    st.subheader("Hi, I ama Sid")
    st.title("A data analyis")

    st.write(" I am jdb,je")
    st.write(" I am jdb,je")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(" What I do")
        st.write("##")
        st.write(
            """
            Batman has an insanely busy schedule. 
            Not only does spend every night patrolling Gotham City for escaped lunatics like the Joker and Two-Face, he also has to spend his days in boardroom meetings at Wayne Enterprises. 
            Then there are those regular Justice League meetings and the time he has to spend on his regular workouts and training sessions with the latest Robin. 
            Even when he’s not Batman, he has to keep up appearances as Bruce Wayne by dating supermodels (poor guy).
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/watch?v=fVeI5xcnsd8&pp=ygUbc29tZXRoaW5nIGluIHRoZSB3YXkgYmF0bWFu)")





