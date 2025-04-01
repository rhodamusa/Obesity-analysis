import streamlit as st
import joblib
import numpy as np

# Load the trained model (ensure it's a pipeline or preprocess manually if needed)
RO = joblib.load('Obesity_model_lr.model')

# Create columns for input fields
col1, col2, col3, col4 = st.columns(4)

# Input fields (adjusted labels and added step for float values)
Gender = col1.number_input(label="Input client's gender", min_value=0, max_value=1)
Age = col2.number_input(label="Input client's Age", min_value=14, max_value=61, step=1)
Height = col3.number_input(label="Input client's Height", min_value=145.0, max_value=198.0, step=0.01)
Weight = col4.number_input(label="Input client's Weight (in kg)", min_value=39.0, max_value=173.0, step=0.1)
family_history_with_overweight = col1.number_input(label="Family history with overweight", min_value=0, max_value=1)
FAVC = col2.number_input(label="Frequent high-calorie food consumption (FAVC)", min_value=0, max_value=1)
FCVC = col3.number_input(label="Frequency of vegetable consumption (FCVC)", min_value=0.0, max_value=3.0, step=0.1)
NCP = col4.number_input(label="Number of main meals (NCP)", min_value=1, max_value=4)
CAEC = col1.number_input(label="Consumption of food between meals (CAEC)", min_value=0, max_value=3)
SMOKE = col2.number_input(label="Smoking habits (0=No, 1=Yes)", min_value=0, max_value=1)
CH2O = col3.number_input(label="Water consumption (CH2O)", min_value=1.0, max_value=3.0, step=0.1)
SCC = col4.number_input(label="Calories monitoring (SCC)", min_value=0, max_value=1)
FAF = col1.number_input(label="Physical activity frequency (FAF,)", min_value=0.0, max_value=3.0, step=0.1)
TUE = col2.number_input(label="Time using technology devices (TUE)", min_value=0.0, max_value=2.0, step=0.1)
CALC = col3.number_input(label="Alcohol consumption (CALC)", min_value=0, max_value=3)
MTRANS = col4.number_input(label="Transportation used (MTRANS)", min_value=1, max_value=4)

# Prediction mapping (check your model's classes_ if unsure)
prediction_mapping = {
    0: "The client is classified as having insufficient weight",
    1: "The client is classified as having normal weight",
    2: "The client is classified as having obesity (Type I)",
    3: "The client is classified as having obesity (Type II)",
    4: "The client is classified as having obesity (Type III)",
    5: "The client is classified as overweight (Level I)",
    6: "The client is classified as overweight (Level II)"
}

# Prediction button
if st.button('Predict'):
    try:
        input_data = np.array([[
            Gender, Age, Height, Weight, family_history_with_overweight,
            FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, MTRANS
        ]])

        with st.spinner("Predicting"):
            OB_prediction = RO.predict(input_data)[0]

        st.success(prediction_mapping.get(OB_prediction, "Prediction not recognized."))

    except Exception as e:
        st.error(f"An error occurred: {e}")
