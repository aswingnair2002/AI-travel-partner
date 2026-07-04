import streamlit as st

from services.gemini_service import generate_itinerary
from prompts.itinerary_prompt import create_prompt
from services.weather_service import get_weather


st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Planner")

destination = st.text_input("Destination")

days = st.number_input(
    "Days",
    min_value=1,
    max_value=15,
    value=3
)

budget = st.number_input(
    "Budget (₹)",
    min_value=1000,
    value=10000
)

travel_style = st.selectbox(
    "Travel Style",
    [
        "Solo",
        "Family",
        "Friends",
        "Adventure"
    ]
)

interests = st.multiselect(
    "Interests",
    [
        "Food",
        "Nature",
        "History",
        "Adventure",
        "Shopping",
        "Beaches"
    ]
)


# Single button only
if st.button("Generate Plan", key="generate_btn"):

    with st.spinner("Creating your itinerary..."):

        # Get weather information
        weather = get_weather(destination)

        # Show weather card
        if weather:
            st.success(
                f"🌤 {weather['temperature']}°C | "
                f"{weather['description']}"
            )
        else:
            st.warning("Could not fetch weather information.")

        # Create AI prompt
        prompt = create_prompt(
            destination,
            days,
            budget,
            travel_style,
            interests,
            weather
        )

        # Generate itinerary
        result = generate_itinerary(prompt)

        st.markdown(result)