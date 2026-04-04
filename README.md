# 🌧️ VibeRain – Gen‑Z Weather Prediction System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://weather-forcast-ty7smv688xghdqc3euqnfa.streamlit.app/)
[![GitHub stars](https://img.shields.io/github/stars/Srishtikumari510/Rain_Rain_When_will_u_come?style=social)](https://github.com/Srishtikumari510/Rain_Rain_When_will_u_come/stargazers)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)

> **Rain or nah?** VibeRain tells you if it's going to rain and suggests outfit colors, movies, and music based on the weather. Built with Machine Learning + Streamlit – fully Gen‑Z approved 💅

🔗 **Live Demo:** [VibeRain on Streamlit](https://weather-forcast-ty7smv688xghdqc3euqnfa.streamlit.app/)

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Installation & Local Setup](#-installation--local-setup)
- [Model Training](#-model-training)
- [Deployment](#-deployment)
- [Screenshots](#-screenshots)
- [Future Work](#-future-work)
- [Team](#-team)
- [License](#-license)

---

## 📖 Overview
VibeRain is a weather prediction application that uses a **Random Forest classifier** (88.6% accuracy) to forecast rain based on five meteorological inputs:
- Temperature (°C)
- Humidity (%)
- Wind Speed (km/h)
- Cloud Cover (%)
- Pressure (hPa)

Unlike boring weather apps, VibeRain adds a **lifestyle twist**: it recommends outfit colors and activities (movies, music, indoor/outdoor) to match the predicted weather and temperature.

---

## ✨ Features
- 🔮 **Rain prediction** with confidence score  
- 👗 **Outfit color suggestions** (rainy → moody colors, sunny → pastels, etc.)  
- 🎬 **Activity recommendations** – movies, music, and things to do  
- 🌈 **Gen‑Z UI** – gradient background, glassmorphism, sliders, balloons & snow animations  
- 📱 **Two‑page navigation** – intro landing + main predictor  
- ☁️ **Deployed on Streamlit Cloud** – accessible 24/7  

---

## 🧰 Tech Stack
| Area | Technologies |
|------|--------------|
| **Frontend** | Streamlit (Python) |
| **Backend / ML** | Python, scikit‑learn, XGBoost, joblib |
| **Data Processing** | Pandas, NumPy |
| **Development** | Google Colab, Jupyter Notebook |
| **Deployment** | Streamlit Cloud, GitHub |
| **Version Control** | Git |

---

## 📊 Dataset
- **Source:** [Weather Forecast Dataset](https://www.kaggle.com/datasets/zeeshier/weather-forecast-dataset) (Kaggle)  
- **Size:** 2500 records, 6 columns  
- **Target:** `Rain` (binary: `rain` / `no rain`)  
- **Features:** Temperature, Humidity, Wind_Speed, Cloud_Cover, Pressure  

All preprocessing (encoding, scaling, train‑test split) was performed in Google Colab.

---

## 📁 Project Structure
