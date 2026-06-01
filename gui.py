import streamlit as st
import pandas as pd
import joblib
import fertilizer

model = joblib.load("crop_model.pkl")

st.set_page_config(page_title="Smart Agriculture AI", layout="centered")

st.title("🌱 Crop Recommendation System")

st.write("Enter soil and weather values:")

n = st.number_input("Nitrogen (N)", min_value=0.0)
p = st.number_input("Phosphorus (P)", min_value=0.0)
k = st.number_input("Potassium (K)", min_value=0.0)
temp = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Value")
rain = st.number_input("Rainfall (mm)")

if st.button("Predict"):

    sample = pd.DataFrame({
        "N": [n],
        "P": [p],
        "K": [k],
        "temperature": [temp],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rain]
    })

    crop = model.predict(sample)[0]
    fert = fertilizer.get_fertilizer(crop)

    st.success(f"Recommended Crop: {crop}")
    st.info(f"Recommended Fertilizer: {fert}")
