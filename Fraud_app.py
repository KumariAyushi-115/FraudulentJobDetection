import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pre-trained model using pickle
with open('trained_model_fraudulentcheck.sav', 'rb') as file:
    model = pickle.load(file)

# Set page title
st.title('Job Fraud Detection System')

# Function to take user input
def user_input():
    # Create input fields for each feature
    job_id = st.number_input('Job ID', min_value=1, step=1, format="%d")
    title = st.text_input('Job Title')
    location = st.number_input('Location (ID)', min_value=0, step=1, format="%d")
    department = st.text_input('Department')
    salary_range = st.number_input('Salary Range (ID)', min_value=0, step=1, format="%d")
    company_profile = st.text_area('Company Profile')
    description = st.text_area('Job Description')
    requirements = st.text_area('Job Requirements')
    benefits = st.text_area('Benefits')
    telecommuting = st.selectbox('Telecommuting (1 = Yes, 0 = No)', [1, 0])
    has_company_logo = st.selectbox('Has Company Logo (1 = Yes, 0 = No)', [1, 0])
    has_questions = st.selectbox('Has Screening Questions (1 = Yes, 0 = No)', [1, 0])
    employment_type = st.number_input('Employment Type (ID)', min_value=0, step=1, format="%d")
    required_experience = st.number_input('Required Experience (ID)', min_value=0, step=1, format="%d")
    required_education = st.number_input('Required Education (ID)', min_value=0, step=1, format="%d")
    industry = st.text_input('Industry')
    function = st.text_input('Job Function')

    # Collect all inputs into a dictionary
    data = {
        'job_id': job_id,
        'title': title,
        'location': location,
        'department': department,
        'salary_range': salary_range,
        'company_profile': company_profile,
        'description': description,
        'requirements': requirements,
        'benefits': benefits,
        'telecommuting': telecommuting,
        'has_company_logo': has_company_logo,
        'has_questions': has_questions,
        'employment_type': employment_type,
        'required_experience': required_experience,
        'required_education': required_education,
        'industry': industry,
        'function': function
    }
    
    # Convert dictionary to a pandas DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Display user input fields and capture the inputs
input_data = user_input()

# Button to make prediction
if st.button('Predict Fraudulence'):
    # Use the loaded model to predict the outcome
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 1:
        st.error('This job posting is predicted as Fraudulent.')
    else:
        st.success('This job posting is predicted as Legitimate.')
