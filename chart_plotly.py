import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    "City": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
    "Population": [19, 18, 11, 14]
}
df = pd.DataFrame(data)

fig = px.bar(df, x="City", y="Population", title="City Population")
st.plotly_chart(fig)