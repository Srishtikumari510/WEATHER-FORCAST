import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('weather_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Rain Predictor", page_icon="🌦️")
st.title("🌧️ Will it Rain?")
st.markdown("Enter the weather conditions below:")

col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=22.5, step=0.5)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=65.0, step=1.0)
    wind = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=50.0, value=10.0, step=0.5)

with col2:
    cloud = st.number_input("Cloud Cover (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1013.0, step=1.0)

if st.button("Predict Rain"):
    input_data = np.array([[temp, humidity, wind, cloud, pressure]])
    input_scaled = scaler.transform(input_data)
    
    # Get probability
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_scaled)[0]
        rain_prob = proba[1]  # probability of class 1 (rain)
        pred = 1 if rain_prob > 0.5 else 0   # threshold 0.5
    else:
        pred = model.predict(input_scaled)[0]
        rain_prob = None
    
    # Display probability and prediction
    st.write(f"**Rain probability:** {rain_prob:.3f}" if rain_prob else "")
    
    if pred == 1:
        st.error(f"🌧️ **Rain expected!** (confidence: {rain_prob:.2%})")
        if rain_prob:
            st.progress(int(rain_prob * 100))
    else:
        st.success(f"☀️ **No rain expected!** (confidence: {1-rain_prob:.2%})")
        if rain_prob:
            st.progress(int((1-rain_prob) * 100))
    
    # Debug: show scaled input values
    with st.expander("Debug info"):
        st.write("Raw input:", [temp, humidity, wind, cloud, pressure])
        st.write("Scaled input:", input_scaled[0])
