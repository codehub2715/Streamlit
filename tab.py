import streamlit as st

st.title("Tab Example")

tab1, tab2, tab3 = st.tabs(["Home", "About", "Contact"])

with tab1:
    st.write("Welcome to Home Page")

with tab2:
    st.write("About Section")

with tab3:
    st.write("Contact: example@mail.com")

col1, col2 = st.columns(2)

with col1:
    st.write("Left column area")
with col2:
    st.write("Right column area")

#Expander components
with st.expander("View Details"):
    st.write("This content is inside an expander box.")