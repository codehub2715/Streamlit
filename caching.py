import streamlit as st

import time

@st.cache_data
def heavy_task():
    time.sleep(2)
    return "Task Completed"

st.write(heavy_task())