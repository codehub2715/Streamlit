import pandas as pd
import streamlit as st

uploaded = st.file_uploader("Upload CSV File", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("CSV Uploaded Successfully")
    st.dataframe(df)