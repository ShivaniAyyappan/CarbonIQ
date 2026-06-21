import streamlit as st
from carbon_calculator import (
    calculate_carbon_footprint,
    carbon_iq_score
)

st.set_page_config(page_title="CarbonIQ")

st.title("🌍 CarbonIQ")
st.subheader(
    "AI-Powered Personal Carbon Emission Forecasting and Sustainability Recommendations"
)

transport_km = st.number_input(
    "Daily Travel Distance (km)",
    min_value=0.0
)

vehicle_type = st.selectbox(
    "Transport Mode",
    [
        "Petrol Car",
        "Diesel Car",
        "Electric Vehicle",
        "Bus",
        "Train",
        "Bike",
        "Walking"
    ]
)

electricity_kwh = st.number_input(
    "Monthly Electricity Usage (kWh)",
    min_value=0.0
)

diet_type = st.selectbox(
    "Diet Type",
    [
        "Vegetarian",
        "Mixed",
        "Non-Vegetarian"
    ]
)

shopping_orders = st.number_input(
    "Online Orders Per Month",
    min_value=0
)

if st.button("Calculate CarbonIQ"):
    result = calculate_carbon_footprint(
        transport_km,
        vehicle_type,
        electricity_kwh,
        diet_type,
        shopping_orders
    )

    score = carbon_iq_score(result["total"])

    st.success(
        f"Total Carbon Footprint: {result['total']} tons CO₂/year"
    )

    st.metric(
        "CarbonIQ Score",
        f"{score}/100"
    )

    st.subheader("Emission Breakdown")

    st.write(f"🚗 Transportation: {result['transport']} tons")
    st.write(f"⚡ Energy: {result['energy']} tons")
    st.write(f"🍽️ Food: {result['food']} tons")
    st.write(f"🛒 Shopping: {result['shopping']} tons")