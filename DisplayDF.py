import streamlit as st
import pandas as pd

data = {
    "Name": ["Amit", "Meera", "John"],
    "Marks": [78, 85, 92]
}
df = pd.DataFrame(data)

st.write("Student Data Table")
st.dataframe(df)