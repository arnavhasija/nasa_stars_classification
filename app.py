import streamlit as st
import numpy as np
import joblib

# Load the trained XGBoost model
model = joblib.load('xgboost_model.joblib')

# Feature names
feature_names = ['redshift', 'u_redshift', 'z_redshift', 'i_redshift', 'r_i', 'g_redshift', 'r_redshift',
                 'g', 'g_r', 'u', 'u_g', 'r', 'z', 'i', 'i_z', 'delta', 'alpha']

# Default values for features
default_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Display feature descriptions and input fields
st.title("Galaxy Classification App")
st.write("Please input the following features:")

# Input fields for user-selected features
user_features = []
for i in range(len(feature_names)):
    if feature_names[i] in ['redshift', 'u_redshift', 'z_redshift', 'i_redshift', 'r_i', 'g_redshift', 'r_redshift']:
        user_input = st.number_input(f"{feature_names[i]}:", value=default_values[i], step=0.01)
        user_features.append(user_input)
    else:
        user_features.append(default_values[i])

# Make a prediction
if st.button("Predict"):
    features = np.array(user_features).reshape(1, -1)
    prediction = model.predict(features)[0]

    # Convert prediction to human-readable label
    if prediction == 0:
        prediction_label = 'GALAXY'
    elif prediction == 1:
        prediction_label = 'QSO'
    else:
        prediction_label = 'STAR'
    
    st.write(f"Predicted Class: {prediction_label}")