import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Anlyxer App")

upload = st.file_uploader("Upload CSV Dataset", type="csv")
if upload:
    df = pd.read_csv(upload)
    st.write("Preview Data")
    st.dataframe(df)

    st.write("Column Summary")
    st.write(df.describe())

    col = st.selectbox("Select Column for Chart", df.select_dtypes(include=['int64', 'float64']).columns)
    fig = px.line(df,y = col,title = f"Trend of {col}")
    st.plotly_chart(fig)
    
    st.write("Bar Chart of Selected Column")
    fig2 = px.bar(df, y=col)
    st.plotly_chart(fig2)


#mini task
    st.write("Pie Chart of Selected Column")
    col1= st.selectbox("Select Column for Pie Chart", df.select_dtypes(include=['object']).columns)
    col2 = st.selectbox("Select Column for Values", df.select_dtypes(include=['int64', 'float64']).columns)
    fig3 = px.pie(df, names=col1, values=col2)
    st.plotly_chart(fig3)

