import streamlit as st

st.title("Sidebar Example")
name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter age", 1, 100)
course = st.sidebar.selectbox("Select a course", ["Python", "Streamlit", "Data Science"])

st.write("Output:")
if name:
    st.write(f"Name: {name}, Age: {age}, Course: {course}")