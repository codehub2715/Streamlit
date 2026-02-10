import streamlit as st

st.title("Hello, Streamlit! ")

st.write("This is my first Streamlit app.")

number = st.slider("Select a number", 0, 10, 5)
st.write("You selected:", number)

name = st.text_input("Enter your name")
if name:
    st.write("Welcome,", name)

#Adding Simple Layout
col1, col2 =st.columns(2)
with col1:
    st.header("Left column")
    st.write("You can put text, charts, etc. here.")
with col2:
    st.header("Right column")
    st.write("This is the right side.")