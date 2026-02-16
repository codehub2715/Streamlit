#Feedback Review System

import streamlit as st
import pandas as pd

st.title("Feedback Review System")

if 'feedback_list' not in st.session_state:
    st.session_state.feedback_list = []

with st.form('feedback_from'):
    user = st.text_input("Enter your Name :")
    rate = st.slider('Rating' , 1,10)
    msg = st.text_area('Feedback Message')
    send = st.form_submit_button('Send')
    
if send:
    st.session_state.feedback_list.append({
        'Name': user,
        'Rating': rate,
        'Message': msg
    })
    st.success('Feedback Saved')

st.write('All Feedbacks:')
for f in st.session_state.feedback_list:
    st.write(f"Name: {f['Name']} | Rating: {f['Rating']} | Message: {f['Message']}")

#Delete button
if st.button("Remove All Feedback"):
    st.session_state.feedback_list = []

#Download CSV
df = pd.DataFrame(st.session_state.feedback_list)
df.to_csv('feedback.csv')
st.download_button('Download', data=df.to_csv(index=False), file_name='feedback.csv')

