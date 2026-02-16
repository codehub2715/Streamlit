import streamlit as st

st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("Student Dashboard Application")

st.sidebar.header("Student Details")
name = st.sidebar.text_input("Full Name")
age = st.sidebar.number_input("Age", 10, 60)
branch = st.sidebar.selectbox("Department", ["Computer Science", "IT", "AI/ML", "ECE"])
level = st.sidebar.radio("Skill Level", ["Beginner", "Intermediate", "Advanced"])
show = st.sidebar.button("Display Profile")

home, skills, feedback, = st.tabs(["Home", "Skills", "Feedback"])

with home:
    st.subheader("Student Profile Summary")
    if show:
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Name: {name}")
            st.write(f"Age: {age}")
        with col2:
            st.write(f"Department: {branch}")
            st.write(f"Level: {level}")
    else:
        st.info("Fill sidebar and click Display Profile")

with skills:
    st.subheader("Rate Skills")
    python = st.slider("Python Skill", 0, 10, 5)
    ml = st.slider("Machine Learning", 0, 10, 4)
    web = st.slider("Web Development", 0, 10, 7)
    communicate = st.slider("Communication Skills", 0,10,8)
    st.write("Skill Summary:")
    st.write(f"Python: {python}/10  |  ML: {ml}/10  |  Web: {web}/10 | communicate: {communicate}/10")
#Then calculate and display average score below all sliders.
    st.write(f"Average skill score: {(python+ml+web+communicate)/4}/10")

with feedback:
    st.subheader("Submit Feedback")
    fb = st.text_area("Write feedback")
    if st.button("Submit"):
        st.success("Feedback Submitted Successfully")