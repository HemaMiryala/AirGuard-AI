import streamlit as st
import joblib
import datetime
import pandas as pd
import time
import os

from utils.api import get_air_quality, get_weather
from utils.aqi import get_aqi_category_info, get_trend
from utils.charts import plot_pollutant_bar_chart, plot_pollutant_pie_chart, plot_aqi_gauge
from utils.recommendations import (
    get_dynamic_health_recommendations,
    get_dynamic_environmental_suggestions,
    get_pollutant_explanations,
    get_pollutant_interactions,
    get_risk_assessment,
    get_forecast_summary
)
from utils.ui_components import get_custom_css, get_hero_section, get_footer

# ==========================================================
# PAGE CONFIG & CSS
# ==========================================================
st.set_page_config(
    page_title="AirGuard AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# ==========================================================
# LOAD MODEL & FEATURES
# ==========================================================
@st.cache_resource
def load_models():
    try:
        model = joblib.load("models/airguard_ai_model.pkl")
        features = joblib.load("models/airguard_features.pkl")
        return model, features
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

model, features = load_models()

# ==========================================================
# HEADER
# ==========================================================
st.markdown(get_hero_section(), unsafe_allow_html=True)
st.divider()

# ==========================================================
# SIDEBAR SETTINGS
# ==========================================================
st.sidebar.title("⚙ Prediction Settings")

today = datetime.datetime.now()
date = today.day
month = today.month
year = today.year
days = today.weekday() + 1

st.sidebar.info(f"📅 Today\n\n{today.strftime('%d %B %Y')}")

station = st.sidebar.selectbox(
    "📍 Select Monitoring Station",
    ["Dwarka (NSUT)", "ITO"]
)

holiday = st.sidebar.radio(
    "🎉 Is Today a Holiday?",
    ["No", "Yes"]
)

holiday_count = 1 if holiday == "Yes" else 0

# Convert Location
if station == "Dwarka (NSUT)":
    lat, lon = 28.608605, 77.035243
    station_ito, station_nsut = 0, 1
else:
    lat, lon = 28.6326, 77.2317
    station_ito, station_nsut = 1, 0

# ==========================================================
# MAIN APP LOGIC
# ==========================================================
predict = st.button("🔍 Predict Tomorrow AQI", use_container_width=True)

if predict:
    if model is None:
        st.error("ML Model is missing. Cannot perform prediction.")
        st.stop()

    with st.spinner("Fetching Live Data & Running AI Engine..."):
        # Artificial delay for smooth UX loading animation
        time.sleep(1) 
        
        weather_data = get_weather(lat, lon)
        air_data = get_air_quality(lat, lon)

    if not air_data:
        st.error("⚠️ Failed to fetch Air Pollution Data from OpenWeather API.")
    else:
        st.success("✅ Real-time data synchronized successfully!")
        
        # ------------------------------------------------------
        # 1. LIVE WEATHER DASHBOARD
        # ------------------------------------------------------
        st.markdown("<br>", unsafe_allow_html=True)
        st.header("🌤 Live Weather Dashboard")
        if weather_data:
            main_weather = weather_data['main']
            wind = weather_data['wind']
            sys = weather_data['sys']
            weather_desc = weather_data['weather'][0]['description'].title()
            weather_icon = weather_data['weather'][0]['icon']
            
            w_col1, w_col2, w_col3, w_col4 = st.columns(4)
            with w_col1:
                st.metric("Temperature", f"{main_weather['temp']} °C", f"{weather_desc}")
            with w_col2:
                st.metric("Feels Like", f"{main_weather['feels_like']} °C")
            with w_col3:
                st.metric("Humidity", f"{main_weather['humidity']} %")
            with w_col4:
                st.metric("Wind Speed", f"{wind['speed']} m/s")
        else:
            st.warning("Weather data currently unavailable.")

        # ------------------------------------------------------
        # 2. AIR POLLUTION DASHBOARD
        # ------------------------------------------------------
        pollution = air_data["list"][0]["components"]
        pm25 = pollution["pm2_5"]
        pm10 = pollution["pm10"]
        no2 = pollution["no2"]
        so2 = pollution["so2"]
        co = pollution["co"]
        ozone = pollution["o3"]
        api_aqi = air_data["list"][0]["main"]["aqi"]
        
        # API returns 1-5 index, rough mapping to real AQI
        aqi_map = {1: 45, 2: 95, 3: 155, 4: 255, 5: 350}
        current_aqi = aqi_map.get(api_aqi, 100)
        
        curr_cat, curr_color, curr_emoji, _, _ = get_aqi_category_info(current_aqi)

        st.divider()
        st.header("🌫 Air Pollution Dashboard")
        
        c_aqi1, c_aqi2 = st.columns([1, 2])
        with c_aqi1:
            st.markdown(f"""
            <div class="glass-card" style="text-align:center; border-top: 5px solid {curr_color};">
                <h3 style="margin-bottom: 0;">Current AQI</h3>
                <h1 style="font-size: 64px; color: {curr_color}; margin: 10px 0;">{current_aqi}</h1>
                <h4 style="color: #4b5563;">{curr_emoji} {curr_cat}</h4>
            </div>
            """, unsafe_allow_html=True)
            
        with c_aqi2:
            pol_c1, pol_c2, pol_c3 = st.columns(3)
            with pol_c1:
                st.metric("PM2.5", round(pm25, 2))
                st.metric("PM10", round(pm10, 2))
            with pol_c2:
                st.metric("NO₂", round(no2, 2))
                st.metric("SO₂", round(so2, 2))
            with pol_c3:
                st.metric("CO", round(co, 2))
                st.metric("Ozone", round(ozone, 2))

        # ------------------------------------------------------
        # 4. BEAUTIFUL VISUALIZATIONS
        # ------------------------------------------------------
        st.subheader("📊 Pollutant Analytics")
        pollutants_dict = {"PM2.5": pm25, "PM10": pm10, "NO2": no2, "SO2": so2, "CO": co, "O3": ozone}
        
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.plotly_chart(plot_pollutant_bar_chart(pollutants_dict), use_container_width=True)
        with chart_col2:
            st.plotly_chart(plot_pollutant_pie_chart(pollutants_dict), use_container_width=True)

        # ------------------------------------------------------
        # 3. AI PREDICTION SECTION
        # ------------------------------------------------------
        input_df = pd.DataFrame([[
            date, month, year, holiday_count, days,
            pm25, pm10, no2, so2, co, ozone,
            station_ito, station_nsut
        ]], columns=features)
        
        prediction = model.predict(input_df)[0]
        predicted_aqi = int(round(prediction))
        
        pred_cat, pred_color, pred_emoji, health_effect, req_action = get_aqi_category_info(predicted_aqi)
        trend_msg, trend_color = get_trend(current_aqi, predicted_aqi)

        st.divider()
        st.header("🤖 AI Prediction Center")
        
        pred_col1, pred_col2 = st.columns([1, 1])
        with pred_col1:
            st.plotly_chart(plot_aqi_gauge(predicted_aqi), use_container_width=True)
            
        with pred_col2:
            st.markdown(f"""
            <div class="glass-card" style="border-left: 6px solid {pred_color};">
                <h3 style="margin-top:0;">Tomorrow's Forecast</h3>
                <h1 style="color: {pred_color}; margin: 10px 0;">{predicted_aqi} ({pred_cat}) {pred_emoji}</h1>
                <h4 style="color: {trend_color}; margin-bottom: 20px;">{trend_msg}</h4>
                <p><strong>Health Risk:</strong> {health_effect}</p>
                <p><strong>Primary Advice:</strong> {req_action}</p>
            </div>
            """, unsafe_allow_html=True)

        # ------------------------------------------------------
        # 5. DYNAMIC RISK ASSESSMENT & INTERACTIONS
        # ------------------------------------------------------
        st.divider()
        risk_assessment = get_risk_assessment(predicted_aqi, pollutants_dict)
        st.subheader("🛡️ Dynamic Risk Assessment")
        st.markdown(f"<div class='glass-card' style='padding: 15px;'>{risk_assessment}</div>", unsafe_allow_html=True)
        
        interactions = get_pollutant_interactions(pollutants_dict)
        if any("⚠️" in interaction for interaction in interactions):
            st.markdown("#### Synergistic Effects")
            for interaction in interactions:
                st.markdown(f"> {interaction}")

        # ------------------------------------------------------
        # 6. HEALTH & ENVIRONMENTAL SUGGESTIONS
        # ------------------------------------------------------
        rec_col1, rec_col2 = st.columns(2)
        
        with rec_col1:
            st.subheader("🏥 Targeted Health Advice")
            health_tips = get_dynamic_health_recommendations(predicted_aqi, pollutants_dict)
            for tip in health_tips:
                st.markdown(f"✅ {tip}")
                
        with rec_col2:
            st.subheader("🌱 Targeted Sustainability Tips")
            env_tips = get_dynamic_environmental_suggestions(predicted_aqi, pollutants_dict)
            for tip in env_tips:
                st.markdown(f"{tip}")
                
        # ------------------------------------------------------
        # 7. DEEP-DIVE POLLUTANT INSIGHTS
        # ------------------------------------------------------
        st.divider()
        st.subheader("🔬 Pollutant Insights (vs WHO Guidelines)")
        explanations = get_pollutant_explanations(pollutants_dict)
        for exp in explanations:
            with st.expander(f"{exp['symbol']} - {exp['status']} ({exp['value']} µg/m³)", expanded=(exp['status'] == 'High')):
                st.markdown(f"**{exp['name']}**")
                st.markdown(f"**Current Value:** {exp['value']} µg/m³ | **WHO Guideline limit:** {exp['threshold']} µg/m³")
                st.markdown(f"**Status:** <span style='color:{exp['status_color']}; font-weight:bold;'>{exp['status']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Description:** {exp['desc']}")
                st.markdown(f"**Major Sources:** {exp['sources']}")
                st.markdown(f"**Health Impacts:** {exp['impacts']}")

        # ------------------------------------------------------
        # 8. SMART PREDICTION SUMMARY
        # ------------------------------------------------------
        st.divider()
        st.subheader("📋 Session Forecast Summary")
        summary_text = get_forecast_summary(predicted_aqi, pred_cat, pollutants_dict)
        st.markdown(f"*{summary_text}*")
        
        summary_data = pd.DataFrame({
            "Date": [today.strftime("%Y-%m-%d")],
            "Station": [station],
            "Current AQI": [current_aqi],
            "Predicted AQI": [predicted_aqi],
            "Category": [pred_cat],
            "Trend": [trend_msg]
        })
        
        st.dataframe(summary_data, use_container_width=True, hide_index=True)
        
        csv = summary_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Summary (CSV)",
            data=csv,
            file_name=f'airguard_summary_{today.strftime("%Y%m%d")}.csv',
            mime='text/csv',
        )

# ==========================================================
# 8. AQI GUIDE SECTION
# ==========================================================
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📖 Interactive AQI Guide"):
    guide = pd.DataFrame({
        "AQI Range": ["0 - 50", "51 - 100", "101 - 200", "201 - 300", "301+"],
        "Category": ["🟢 Good", "🟡 Moderate", "🟠 Poor", "🔴 Very Poor", "🟣 Severe"],
        "Health Impact": [
            "Air quality is excellent.",
            "Acceptable for most people.",
            "Sensitive groups may experience health effects.",
            "Everyone may experience health effects.",
            "Serious health risk for everyone."
        ],
        "Recommended Action": [
            "Enjoy outdoor activities.",
            "Unusually sensitive people should consider reducing prolonged outdoor exertion.",
            "Reduce prolonged or heavy outdoor exertion.",
            "Avoid prolonged or heavy outdoor exertion.",
            "Avoid all physical activity outdoors."
        ]
    })
    st.dataframe(guide, use_container_width=True, hide_index=True)

# ==========================================================
# 9. ABOUT PROJECT SECTION
# ==========================================================
with st.expander("ℹ️ About AirGuard AI"):
    st.markdown("""
    ### 🌍 AirGuard AI
    AirGuard AI is an advanced machine learning dashboard designed to predict tomorrow's Air Quality Index (AQI) based on real-time pollution and weather parameters.

    ### 🎯 Problem Statement
    Air pollution is a silent killer. People often lack immediate knowledge of upcoming pollution trends, preventing them from taking timely health precautions.
    
    ### 💡 Solution
    By leveraging a Random Forest model trained on historical AQI and meteorological data, AirGuard AI provides an accurate forecast and actionable health advice for the community.
    
    ### 🛠 Technologies Used
    - **Frontend:** Streamlit, Custom CSS, Plotly
    - **Backend Engine:** Python, Pandas, Scikit-Learn (Random Forest)
    - **Data Source:** OpenWeather API
    """)

# ==========================================================
# 10. PROFESSIONAL FOOTER
# ==========================================================
st.markdown(get_footer(), unsafe_allow_html=True)