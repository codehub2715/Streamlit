import streamlit as st

with st.form("user_form"):
    name = st.text_input("Name")
    age = st.number_input("Age",1,100)
    submit = st.form_submit_button("Submit")

if submit:
    st.write("Name :",name)
    st.write("Age :",age)
