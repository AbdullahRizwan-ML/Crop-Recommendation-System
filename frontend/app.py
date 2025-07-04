import streamlit as st
import requests

# 🚀 Backend URL
API_URL = "http://127.0.0.1:8000/predict"  # Update to deployed URL if hosted

# 🌾 Title and instructions
st.set_page_config(page_title="Crop Recommendation", page_icon="🌿")
st.title("🌾 Crop Recommendation System")
st.write("Enter soil and weather conditions below to get crop suggestions.")

# 🌿 Input fields
with st.form("crop_form"):
    nitrogen = st.number_input("🧪 Nitrogen (N)", min_value=0, step=1)
    phosphorus = st.number_input("🧪 Phosphorus (P)", min_value=0, step=1)
    potassium = st.number_input("🧪 Potassium (K)", min_value=0, step=1)
    temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, step=0.1)
    humidity = st.number_input("💧 Humidity (%)", min_value=0.0, step=0.1)
    ph = st.number_input("🧫 pH", min_value=0.0, step=0.1)
    rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🚀 Predict Crop")

if submitted:
    payload = {
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            crop = result.get("predicted_crop", "Unknown")
            st.success(f"✅ Recommended Crop: **{crop.title()}**")
        else:
            st.error(f"❌ Error: Received unexpected status code {response.status_code}")
    except Exception as e:
        st.error(f"❌ Error: Could not connect to backend.\n\nDetails: {e}")
