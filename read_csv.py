import pandas as pd
import streamlit as st

# CSV Reading
file = "students.csv"  # local csv file

df = pd.read_csv(file)
st.write("Loaded CSV Data")
st.dataframe(df)