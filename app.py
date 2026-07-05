import importlib
import streamlit as st

from services.gemini_service import generate_itinerary
from services.weather_service import get_weather
from services.image_service import get_destination_images
from services.maps_service import get_google_maps_link
import prompts.itinerary_prompt as itinerary_prompt_module

importlib.reload(itinerary_prompt_module)
create_prompt = itinerary_prompt_module.create_prompt


# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="AI Travel Assistant",
    layout="wide",
    initial_sidebar_state="expanded",
)

HERO_IMAGE = (
    "https://images.unsplash.com/photo-1488646953014-85cb44e25828"
    "?auto=format&fit=crop&w=1600&q=80"
)


# ======================
# CUSTOM CSS
# ======================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

:root {
    --primary: #0f172a;
    --accent: #0d9488;
    --accent-soft: #ccfbf1;
    --surface: #ffffff;
    --muted: #64748b;
    --border: #e2e8f0;
    --bg: #f1f5f9;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

.hero {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    min-height: 220px;
    margin-bottom: 2rem;
    background:
        linear-gradient(135deg, rgba(15, 23, 42, 0.82), rgba(13, 148, 136, 0.55)),
        url('HERO_IMAGE_PLACEHOLDER') center/cover no-repeat;
    display: flex;
    align-items: flex-end;
    padding: 2.5rem;
}

.hero h1 {
    color: #ffffff;
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin: 0 0 0.5rem 0;
    line-height: 1.15;
}

.hero p {
    color: rgba(255, 255, 255, 0.88);
    font-size: 1.05rem;
    margin: 0;
    max-width: 520px;
}

section[data-testid="stSidebar"] {
    background: var(--surface);
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

.sidebar-title {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.25rem;
}

div[data-testid="stMetric"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.1rem;
    box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
}

div[data-testid="stMetric"] label {
    color: var(--muted);
    font-size: 0.78rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: var(--primary);
    font-weight: 600;
}

.weather-banner {
    background: linear-gradient(90deg, #f0fdfa, #ecfeff);
    border: 1px solid #99f6e4;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 1.5rem;
    color: #115e59;
    font-weight: 500;
}

.place-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}

.place-card h4 {
    margin: 0;
    font-size: 0.98rem;
    font-weight: 600;
    color: var(--primary);
}

.place-card span {
    color: var(--muted);
    font-size: 0.82rem;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 1rem;
}

.feature-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
}

.feature-card h3 {
    margin: 0 0 0.35rem 0;
    font-size: 0.95rem;
    color: var(--primary);
}

.feature-card p {
    margin: 0;
    font-size: 0.85rem;
    color: var(--muted);
    line-height: 1.5;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    border-bottom: 1px solid var(--border);
}

.stTabs [data-baseweb="tab"] {
    height: 44px;
    padding: 0 1.25rem;
    font-weight: 500;
    color: var(--muted);
    background: transparent;
    border-radius: 8px 8px 0 0;
}

.stTabs [aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
}

div[data-testid="stImage"] img {
    border-radius: 12px;
    border: 1px solid var(--border);
}

.stButton > button[kind="primary"],
.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: 600;
    padding: 0.65rem 1rem;
    transition: all 0.15s ease;
}

.stButton > button[kind="primary"] {
    background: var(--accent);
    border: 1px solid var(--accent);
}

.stButton > button[kind="primary"]:hover {
    background: #0f766e;
    border-color: #0f766e;
}

div[data-testid="stExpander"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
}

div[data-testid="stExpander"] summary {
    font-weight: 600;
    color: var(--primary);
}

.gallery-caption {
    font-size: 0.75rem;
    color: var(--muted);
    margin-top: 0.35rem;
}

@media (max-width: 768px) {
    .feature-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 1.75rem;
    }
}
</style>
""".replace("HERO_IMAGE_PLACEHOLDER", HERO_IMAGE),
    unsafe_allow_html=True,
)


# ======================
# HELPERS
# ======================

def split_days(text):
    sections = []
    current = []

    for line in text.splitlines():
        if line.strip().startswith("Day"):
            if current:
                sections.append("\n".join(current))
            current = [line]
        else:
            current.append(line)

    if current:
        sections.append("\n".join(current))

    return sections


# ======================
# HERO
# ======================

st.markdown(
    """
    <div class="hero">
        <div>
            <h1>AI Travel Assistant</h1>
            <p>Personalized itineraries powered by AI, live weather, and destination insights.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ======================
# SIDEBAR INPUTS
# ======================

with st.sidebar:
    st.markdown('<p class="sidebar-title">Trip details</p>', unsafe_allow_html=True)

    destination = st.text_input(
        "Destination",
        placeholder="Paris, Tokyo, Munnar...",
        label_visibility="collapsed",
    )

    st.markdown('<p class="sidebar-title">Duration & budget</p>', unsafe_allow_html=True)

    days = st.number_input(
        "Number of days",
        min_value=1,
        max_value=15,
        value=3,
    )

    budget = st.number_input(
        "Budget (INR)",
        min_value=1000,
        value=10000,
        step=1000,
    )

    st.markdown('<p class="sidebar-title">Preferences</p>', unsafe_allow_html=True)

    travel_style = st.selectbox(
        "Travel style",
        [
            "Solo",
            "Family",
            "Friends",
            "Adventure",
            "Couple",
            "Luxury",
            "Backpacking",
        ],
    )

    interests = st.multiselect(
        "Interests",
        [
            "Food",
            "Nature",
            "History",
            "Adventure",
            "Shopping",
            "Beaches",
            "Nightlife",
            "Culture",
            "Photography",
        ],
    )

    generate = st.button("Generate travel plan", type="primary", use_container_width=True)


# ======================
# MAIN CONTENT
# ======================

if not generate:
    st.markdown("### Plan your next journey")
    st.caption("Fill in your trip details in the sidebar, then generate a tailored itinerary.")

    st.markdown(
        """
        <div class="feature-grid">
            <div class="feature-card">
                <h3>Smart itineraries</h3>
                <p>Day-by-day plans with activities, dining, and lodging tailored to your style.</p>
            </div>
            <div class="feature-card">
                <h3>Live weather</h3>
                <p>Current conditions at your destination so plans stay practical and comfortable.</p>
            </div>
            <div class="feature-card">
                <h3>Local highlights</h3>
                <p>Curated places to visit with direct links to maps for easy navigation.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif not destination:
    st.error("Please enter a destination to continue.")

else:
    with st.spinner("Building your personalized travel plan..."):
        weather = get_weather(destination)

        if weather:
            st.markdown(
                f"""
                <div class="weather-banner">
                    Current conditions in {destination}: {weather['temperature']}°C,
                    {weather['description'].title()}
                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Temperature", f"{weather['temperature']}°C")
            with col2:
                st.metric("Humidity", f"{weather['humidity']}%")
            with col3:
                st.metric("Wind", f"{weather['wind_speed']} m/s")
        else:
            st.warning("Weather data is unavailable for this destination.")

        prompt = create_prompt(
            destination=destination,
            days=days,
            budget=budget,
            travel_style=travel_style,
            interests=interests,
            weather=weather,
        )

        result = generate_itinerary(prompt)
        images = get_destination_images(destination)

        places = [
            ("Landmark & attractions", f"Top sights in {destination}"),
            ("Markets & shopping", f"Popular markets in {destination}"),
            ("Historic district", f"Heritage areas in {destination}"),
            ("Scenic spots", f"Best views in {destination}"),
            ("Food & dining", f"Local cuisine in {destination}"),
        ]

        st.markdown(f"### Your trip to {destination}")
        st.caption(
            f"{days} days · {travel_style} · Budget ₹{budget:,}"
            + (f" · Interests: {', '.join(interests)}" if interests else "")
        )

        itinerary_tab, gallery_tab, places_tab = st.tabs(
            ["Itinerary", "Gallery", "Places"]
        )

        with itinerary_tab:
            st.markdown("#### Personalized itinerary")
            day_sections = split_days(result)

            if len(day_sections) > 1:
                for section in day_sections:
                    title = section.split("\n")[0]
                    content = "\n".join(section.split("\n")[1:])

                    with st.expander(title, expanded=True):
                        st.markdown(content)
            else:
                st.markdown(result)

        with gallery_tab:
            st.markdown("#### Destination gallery")

            if images:
                cols = st.columns(2)
                for i, image in enumerate(images):
                    with cols[i % 2]:
                        st.image(
                            image["url"],
                            use_container_width=True,
                        )
                        st.markdown(
                            f'<p class="gallery-caption">Photo by {image["photographer"]}</p>',
                            unsafe_allow_html=True,
                        )
            else:
                st.info("No photos found for this destination.")

        with places_tab:
            st.markdown("#### Recommended places")

            for i, (title, subtitle) in enumerate(places):
                place_query = f"{title} in {destination}"
                maps_url = get_google_maps_link(place_query, destination)

                col1, col2 = st.columns([5, 1])
                with col1:
                    st.markdown(
                        f"""
                        <div class="place-card">
                            <div>
                                <h4>{title}</h4>
                                <span>{subtitle}</span>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                with col2:
                    st.link_button(
                        "Map",
                        maps_url,
                        key=f"map_{i}",
                        use_container_width=True,
                    )
