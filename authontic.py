#Authontication System

import streamlit as st
users = {'admin':'1234','test': '1111'}

user = st.text_input("User Name")
password = st.text_input("Password",type='password')

if st.button("Login"):
    if user in users and users[user] == password:
        st.session_state.logged = True
        st.write("Login Successful")
    else:
        st.write("Invalid Creditials")
        
