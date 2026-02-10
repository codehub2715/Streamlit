#Create a new Streamlit app with the following features:

#- Title: "Student Info App"
#- A text input to enter student name.
#- A number input to enter student age.
#- A selectbox to choose course (e.g., Python, Data Science, Web Development).
#- When user fills details, display a summary like: "Hi [name], age [age], you selected [course]."

import streamlit as st

st.title("Student Info APP")

name = st.text_input("Enter your name: ")
age = st.number_input("Enter your age: ")

course = st.selectbox("Select your course: ",["Python", "Data Science", "Web Development"])

if st.button("Submit"):
    st.write(f"Hi {name}, your age is {age} and you are Selected in {course}.")
