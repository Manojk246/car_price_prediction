import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and scaler
with open("trained_car.sav", "rb") as f:
    model = pickle.load(f)

with open("scaler.sav", "rb") as f:
    scaler = pickle.load(f)

st.title("🚗 Car Price Predictor")

st.write("Enter car features to estimate the price (in ₹1000s).")

# Example inputs (replace with your actual dataset features)
year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
mileage = st.number_input("Mileage (in km)", min_value=0, max_value=500000, value=50000)
engine_size = st.number_input("Engine Size (cc)", min_value=500, max_value=6000, value=1500)
fuel_type = st.number_input("Fuel Type (numeric encoding)", min_value=0, max_value=5, value=1)
transmission = st.number_input("Transmission (numeric encoding)", min_value=0, max_value=2, value=0)
doors = st.number_input("Number of Doors", min_value=2, max_value=6, value=4)
owners = st.number_input("Previous Owners", min_value=0, max_value=10, value=1)
horsepower = st.number_input("Horsepower", min_value=30, max_value=1000, value=120)
torque = st.number_input("Torque", min_value=50, max_value=2000, value=250)
weight = st.number_input("Car Weight (kg)", min_value=500, max_value=5000, value=1200)

# Create feature array
features = np.array([[year, mileage, engine_size, fuel_type, transmission,
                      doors, owners, horsepower, torque, weight]])

# Scale features
features_scaled = scaler.transform(features)

if st.button("Predict Price"):
    prediction = model.predict(features_scaled)
    st.success(f"Estimated Car Price: ₹{prediction[0]:,.2f}k")
