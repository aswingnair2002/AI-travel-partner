import streamlit as st

from services.gemini_service import generate_itinerary
from services.weather_service import get_weather
from services.image_service import get_destination_images
from services.maps_service import get_google_maps_link
from prompts.itinerary_prompt import create_prompt


# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Planner")
st.write("Plan smart trips with AI and real-time data.")


# ======================
# USER INPUTS
# ======================

destination = st.text_input(
    "📍 Destination",
    placeholder="e.g. Paris, Munnar, Tokyo"
)

days = st.number_input(
    "📅 Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

budget = st.number_input(
    "💰 Budget (₹)",
    min_value=1000,
    value=10000,
    step=1000
)

travel_style = st.selectbox(
    "🧳 Travel Style",
    [
        "Solo",
        "Family",
        "Friends",
        "Adventure",
        "Couple",
        "Luxury",
        "Backpacking"
    ]
)

interests = st.multiselect(
    "🎯 Interests",
    [
        "Food",
        "Nature",
        "History",
        "Adventure",
        "Shopping",
        "Beaches",
        "Nightlife",
        "Culture",
        "Photography"
    ]
)


# ======================
# GENERATE BUTTON
# ======================

if st.button("🚀 Generate Plan", key="generate_btn"):

    if not destination:

        st.error("Please enter a destination.")

    else:

        with st.spinner("Generating your AI travel plan..."):

            # ======================
            # WEATHER
            # ======================

            weather = get_weather(destination)

            if weather:

                st.success(
                    f"🌤 {weather['temperature']}°C | "
                    f"{weather['description'].title()}"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "🌡 Temperature",
                        f"{weather['temperature']}°C"
                    )

                with col2:
                    st.metric(
                        "💧 Humidity",
                        f"{weather['humidity']}%"
                    )

                with col3:
                    st.metric(
                        "💨 Wind",
                        f"{weather['wind_speed']} m/s"
                    )

            else:

                st.warning(
                    "Could not fetch weather information."
                )

            # ======================
            # DESTINATION IMAGES
            # ======================

            st.subheader("📸 Destination Gallery")

            images = get_destination_images(destination)

            if images:

                cols = st.columns(2)

                for i, image in enumerate(images):

                    with cols[i % 2]:

                        st.image(
                            image["url"],
                            caption=f"Photo by {image['photographer']}",
                            use_container_width=True
                        )

            else:

                st.info(
                    "No images found for this destination."
                )

            # ======================
            # PLACES TO VISIT
            # ======================

            st.subheader("📍 Recommended Places")

            # Temporary demo list
            # Later, replace this with Google Places API
            places = [
                f"Top attraction in {destination}",
                f"Famous market in {destination}",
                f"Historic center of {destination}",
                f"Popular beach in {destination}",
                f"Local food street in {destination}"
            ]

            for i, place in enumerate(places):

                maps_url = get_google_maps_link(
                    place,
                    destination
                )

                col1, col2 = st.columns([4, 1])

                with col1:
                    st.write(f"⭐ **{place}**")

                with col2:
                    st.link_button(
                        "🗺 Open",
                        maps_url,
                        key=f"map_{i}"
                    )

            # ======================
            # CREATE AI PROMPT
            # ======================

            prompt = create_prompt(
                destination,
                days,
                budget,
                travel_style,
                interests,
                weather
            )

            # ======================
            # GEMINI RESPONSE
            # ======================

            result = generate_itinerary(prompt)

            st.divider()

            st.subheader("🗺 Your Personalized Itinerary")

            st.markdown(result)