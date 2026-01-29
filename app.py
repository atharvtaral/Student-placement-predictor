import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('placement_rf_model.pkl', 'rb'))

# Set the page title
st.set_page_config(page_title="Student Placement Predictor")

st.title("🎓 Student Placement Prediction System")
st.markdown("Enter the student's details below to predict their placement status.")

# Create two columns for a better layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=30, value=20)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
    internships = st.number_input("Number of Internships", min_value=0, max_value=5, value=0)
    projects = st.number_input("Number of Projects", min_value=0, max_value=10, value=2)
    backlogs = st.number_input("Number of Backlogs", min_value=0, max_value=10, value=0)

with col2:
    coding_skills = st.slider("Coding Skills (1-10)", 1, 10, 5)
    comm_skills = st.slider("Communication Skills (1-10)", 1, 10, 5)
    aptitude_score = st.number_input("Aptitude Test Score (0-100)", 0, 100, 70)
    soft_skills = st.slider("Soft Skills Rating (1-10)", 1, 10, 5)
    certifications = st.number_input("Certifications", 0, 10, 1)

# Categorical Inputs
st.subheader("Academic Background")
c1, c2, c3 = st.columns(3)
with c1:
    gender = st.selectbox("Gender", ["Male", "Female"])
with c2:
    degree = st.selectbox("Degree", ["B.Tech", "BCA", "MCA", "B.Sc"])
with c3:
    branch = st.selectbox("Branch", ["Civil", "ECE", "IT", "ME", "CSE"])  # Added CSE as a default logic check

# Prediction Button
if st.button("Predict Placement Status"):
    # 1. Create a dictionary of input data
    # Note: We must match the EXACT column names and order your model was trained on
    input_data = {
        'Age': age, 'CGPA': cgpa, 'Internships': internships, 'Projects': projects,
        'Coding_Skills': coding_skills, 'Communication_Skills': comm_skills,
        'Aptitude_Test_Score': aptitude_score, 'Soft_Skills_Rating': soft_skills,
        'Certifications': certifications, 'Backlogs': backlogs,
        'Gender_Male': 1 if gender == "Male" else 0,
        'Degree_B.Tech': 1 if degree == "B.Tech" else 0,
        'Degree_BCA': 1 if degree == "BCA" else 0,
        'Degree_MCA': 1 if degree == "MCA" else 0,
        'Branch_Civil': 1 if branch == "Civil" else 0,
        'Branch_ECE': 1 if branch == "ECE" else 0,
        'Branch_IT': 1 if branch == "IT" else 0,
        'Branch_ME': 1 if branch == "ME" else 0
    }

    # 2. Convert to DataFrame
    features = pd.DataFrame([input_data])

    # 3. Predict
    prediction = model.predict(features)[0]

    # 4. Display Result
    if prediction == 1:
        st.success("🎉 Prediction: **PLACED**")
        st.balloons()
    else:
        st.error("⚠️ Prediction: **NOT PLACED**")
        st.info("Tip: Improve CGPA or add more Internships to increase chances.")

    C:\Users\Shree\PycharmProjects\PythonProject1\PythonProject\.venv\student.py