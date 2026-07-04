def create_prompt(
    destination,
    days,
    budget,
    travel_style,
    interests,
    weather=None
):

    weather_text = ""

    if weather:
        weather_text = f"""
Current Weather:
Temperature: {weather['temperature']}°C
Condition: {weather['description']}
Humidity: {weather['humidity']}%
"""

    prompt = f"""
You are an expert travel planner.

Create a {days}-day itinerary.

Destination: {destination}
Budget: ₹{budget}
Travel Style: {travel_style}
Interests: {', '.join(interests)}

{weather_text}

Include:

1. Day-wise plan
2. Morning, afternoon, and evening activities
3. Hotel suggestions
4. Local foods to try
5. Estimated expenses
6. Travel tips
7. If the weather is bad, suggest indoor activities.

Use markdown formatting.
"""

    return prompt