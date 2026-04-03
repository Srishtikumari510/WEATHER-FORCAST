import streamlit as st
import numpy as np
import joblib
import time
import random

# ---------- PAGE CONFIG (shared) ----------
st.set_page_config(
    page_title="VibeRain | rain or nah?",
    page_icon="🌧️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- LOAD MODEL & SCALER (cached) ----------
@st.cache_resource
def load_artifacts():
    model = joblib.load('weather_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_artifacts()

# ---------- SUGGESTION FUNCTIONS ----------
def outfit_suggestion(is_rain, temp):
    if is_rain:
        colors = ["dark blue", "charcoal grey", "black", "olive green", "burgundy"]
        outfit = f"wear something waterproof + a moody {random.choice(colors)} vibe. hoodie & boots >>"
    else:
        if temp > 25:
            colors = ["white", "pastel yellow", "baby blue", "coral"]
            outfit = f"keep it breezy in {random.choice(colors)} – shorts & tee energy ☀️"
        elif temp < 15:
            colors = ["cream", "beige", "soft lavender", "dusty pink"]
            outfit = f"cozy layers in {random.choice(colors)} – cute jacket + scarf moment ✨"
        else:
            colors = ["lavender", "sage green", "terracotta", "peach"]
            outfit = f"vibe in {random.choice(colors)} – jeans and a nice top 🍃"
    return outfit

def activity_suggestions(is_rain, temp, humidity):
    if is_rain:
        movies = ["🏠 " + m for m in ["Eternal Sunshine", "The Notebook", "Ponyo", "Pride & Prejudice (2005)", "Lost in Translation"]]
        music = ["🎧 " + m for m in ["lofi beats", "rainy jazz", "Taylor Swift (folklore)", "Bon Iver", "Frank Ocean"]]
        indoor_activities = ["📖 read a book", "🎮 gaming marathon", "🍜 cook ramen", "🖌️ paint / draw", "📺 binge a K-drama"]
        activity = f"stay cozy indoors! {random.choice(indoor_activities)}. watch {random.choice(movies)} or listen to {random.choice(music)}."
    else:
        if temp > 28:
            movies = ["🎬 " + m for m in ["Mamma Mia!", "Call Me By Your Name", "The Beach", "In the Heights"]]
            music = ["🎧 " + m for m in ["reggaeton", "beach house", "Doja Cat", "Tropical house"]]
            outdoor = ["🏖️ go to the beach/pool", "🍦 get ice cream", "🌳 picnic in the park", "🚴 bike ride"]
        elif temp < 10:
            movies = ["🎬 " + m for m in ["The Holiday", "Little Women", "Into the Wild", "The Secret Life of Walter Mitty"]]
            music = ["🎧 " + m for m in ["indie folk", "Hozier", "The Lumineers", "acoustic playlist"]]
            outdoor = ["☕ coffee shop hop", "🧣 scenic walk", "📸 photography walk", "🛍️ thrift shopping"]
        else:
            movies = ["🎬 " + m for m in ["10 Things I Hate About You", "La La Land", "Palm Springs", "Anyone But You"]]
            music = ["🎧 " + m for m in ["pop punk", "Olivia Rodrigo", "Dua Lipa", "The Weeknd"]]
            outdoor = ["🚶‍♀️ farmers market", "🌿 hiking", "🛹 skatepark", "🎨 outdoor art fair"]
        activity = f"go outside! {random.choice(outdoor)}. then watch {random.choice(movies)} or vibe to {random.choice(music)}."
    return activity

# ---------- PAGE 1: INTRO (Gen‑Z landing) ----------
def intro_page():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,600;14..32,800&display=swap');
        * { font-family: 'Inter', sans-serif; }
        .stApp { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); }
        .intro-card {
            background: rgba(255,255,255,0.08);
            backdrop-filter: blur(14px);
            border-radius: 2rem;
            padding: 2rem;
            text-align: center;
            margin-top: 3rem;
            border: 1px solid rgba(255,255,255,0.15);
        }
        h1 {
            font-size: 3.5rem !important;
            font-weight: 800 !important;
            background: linear-gradient(120deg, #FFDEE9, #B5FFFC);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent !important;
        }
        .glow {
            font-size: 1.2rem;
            color: #ddd;
            margin: 1rem 0;
        }
        .stButton > button {
            background: linear-gradient(90deg, #FF6B6B, #FF8E53);
            color: white;
            font-weight: 700;
            font-size: 1.2rem;
            padding: 0.6rem 2rem;
            border-radius: 3rem;
            border: none;
            width: 80%;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(255,107,107,0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="intro-card">', unsafe_allow_html=True)
    st.markdown("<h1>🌧️ VibeRain</h1>", unsafe_allow_html=True)
    st.markdown('<p class="glow">✨ the only weather app that gets your ✨vibe✨ ✨</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### ☕ what’s the tea?")
    st.markdown("VibeRain tells you if it’s gonna rain AND gives you outfit colors + movie/music recs based on the weather.")
    st.markdown("no boring forecasts — just pure gen‑z energy 💅")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔮 start the vibe check →", use_container_width=False):
        st.session_state.page = "main"
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<footer style='text-align:center; margin-top:3rem; color:#aaa;'>vibes only | no cap</footer>", unsafe_allow_html=True)

# ---------- PAGE 2: MAIN PREDICTOR + SUGGESTIONS ----------
def main_page():
    # Custom CSS for main page
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,600;14..32,800&display=swap');
        * { font-family: 'Inter', sans-serif; }
        .stApp { background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); }
        .main {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(12px);
            border-radius: 2rem;
            padding: 2rem;
            margin: 1rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.1);
        }
        h1 {
            font-size: 3rem !important;
            font-weight: 800 !important;
            background: linear-gradient(120deg, #FFDEE9, #B5FFFC);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent !important;
            text-align: center;
        }
        .subhead { text-align: center; color: #ccc; margin-bottom: 2rem; }
        .stSlider label, .stNumberInput label { font-weight: 600 !important; color: #f0f0f0 !important; }
        .stButton > button {
            background: linear-gradient(90deg, #FF6B6B, #FF8E53);
            color: white;
            font-weight: 700;
            font-size: 1.2rem;
            padding: 0.6rem 2rem;
            border-radius: 3rem;
            border: none;
            width: 100%;
            transition: all 0.3s ease;
        }
        .stButton > button:hover { transform: scale(1.02); }
        .rain-card, .norain-card {
            background: rgba(0,0,0,0.6);
            border-radius: 1.5rem;
            padding: 1.2rem;
            margin-top: 2rem;
            text-align: center;
            backdrop-filter: blur(8px);
        }
        .rain-card { border-left: 5px solid #ff4d4d; }
        .norain-card { border-left: 5px solid #4caf50; }
        .prob-text { font-size: 1.4rem; font-weight: 700; margin-top: 0.5rem; }
        .suggestion-box {
            background: rgba(255,255,255,0.1);
            border-radius: 1rem;
            padding: 0.8rem;
            margin-top: 1rem;
            text-align: left;
        }
        footer { text-align: center; margin-top: 3rem; color: #aaa; font-size: 0.8rem; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown("<h1>🌧️ VibeRain</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subhead">drop the weather deets & get the tea ☕ + outfit inspo 👗🎧</p>', unsafe_allow_html=True)

    # Back button (optional)
    if st.button("← back to intro", use_container_width=False):
        st.session_state.page = "intro"
        st.rerun()

    # Input sliders
    col1, col2 = st.columns(2)
    with col1:
        temp = st.slider("🌡️ temp (°C)", -10.0, 50.0, 22.5, 0.5, format="%.1f")
        humidity = st.slider("💧 humidity (%)", 0, 100, 65, 1, format="%d%%")
        wind = st.slider("💨 wind speed (km/h)", 0.0, 50.0, 10.0, 0.5, format="%.1f")
    with col2:
        cloud = st.slider("☁️ cloud cover (%)", 0, 100, 50, 1, format="%d%%")
        pressure = st.slider("📉 pressure (hPa)", 900, 1100, 1013, 1, format="%d hPa")

    if st.button("🔮 predict my vibe", use_container_width=True):
        input_data = np.array([[temp, humidity, wind, cloud, pressure]])
        input_scaled = scaler.transform(input_data)

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_scaled)[0]
            rain_prob = proba[1]
            pred = 1 if rain_prob > 0.5 else 0
        else:
            pred = model.predict(input_scaled)[0]
            rain_prob = None

        with st.spinner("analyzing the clouds... 🌦️"):
            time.sleep(0.8)

        # Prediction result
        if pred == 1:
            st.markdown(f"""
            <div class="rain-card">
                <div style="font-size:3rem;">🌧️🌀</div>
                <div style="font-size:1.8rem; font-weight:800;">RAIN ALERT ☔</div>
                <div class="prob-text">confidence: {rain_prob:.1%}</div>
                <div>grab an umbrella bestie 💅</div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(int(rain_prob * 100))
            st.balloons()
        else:
            st.markdown(f"""
            <div class="norain-card">
                <div style="font-size:3rem;">☀️✨</div>
                <div style="font-size:1.8rem; font-weight:800;">NO RAIN VIBES</div>
                <div class="prob-text">confidence: {(1-rain_prob):.1%}</div>
                <div>no umbrella needed, slay the day 💅</div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(int((1-rain_prob) * 100))
            st.snow()

        # Suggestions
        is_rain = (pred == 1)
        outfit = outfit_suggestion(is_rain, temp)
        activity = activity_suggestions(is_rain, temp, humidity)

        st.markdown("### ✨ your vibe guide ✨")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"<div class='suggestion-box'>👗 <b>outfit energy</b><br>{outfit}</div>", unsafe_allow_html=True)
        with col_b:
            st.markdown(f"<div class='suggestion-box'>🎬 <b>things to do</b><br>{activity}</div>", unsafe_allow_html=True)

        # Debug expander
        with st.expander("✨ advanced details (for nerds)"):
            st.write("raw inputs:", [temp, humidity, wind, cloud, pressure])
            st.write("scaled values:", input_scaled[0])
            if rain_prob:
                st.write(f"rain probability: {rain_prob:.4f}")

    st.markdown("""
    <footer>
        VibeRain 🌧️ | made with 💜 by a gen‑z dev | rain or nah, we got your fit & plans
    </footer>
    </div>
    """, unsafe_allow_html=True)

# ---------- ROUTING ----------
if "page" not in st.session_state:
    st.session_state.page = "intro"

if st.session_state.page == "intro":
    intro_page()
else:
    main_page()
