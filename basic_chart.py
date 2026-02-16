import streamlit as st
import pandas as pd

data = {
    "Year": [2019, 2020, 2021, 2022],
    "Sales": [150, 200, 250, 300]
}
df = pd.DataFrame(data)

st.line_chart(df.set_index("Year"))
st.bar_chart(df.set_index("Year"))
st.area_chart(df.set_index("Year"))