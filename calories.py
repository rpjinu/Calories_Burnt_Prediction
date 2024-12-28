import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\calories_burnt_prediction\best_calorie_model.pkl")

# Streamlit app configuration
st.set_page_config(page_title="Calories Burnt Prediction", page_icon="🔥")

# Title and description
st.title("🔥 Calories Burnt Prediction API")
st.write("Enter your details to predict the calories burnt.")

# Input fields
gender = st.radio("Gender", options=["Male", "Female"])
age = st.number_input("Age (years)", min_value=1, max_value=120, value=25)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=70.0)
duration = st.number_input("Exercise Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40.0, max_value=200.0, value=100.0)
body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, value=37.5)

# Predict button
if st.button("Predict Calories"):
    # Convert gender to numerical value
    gender_num = 1 if gender == "Female" else 0
    
    # Prepare the input array
    input_data = np.array([[gender_num, age, height, weight, duration, heart_rate, body_temp]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display result
    st.success(f"Estimated Calories Burnt: {prediction[0]:.2f} kcal")
