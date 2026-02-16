import streamlit as st

import pandas as pd 

file = st.file_uploader("Upload Excel File", type=['xlsx'])

if file:
    df = pd.read_excel(file)
    st.dataframe(df)
