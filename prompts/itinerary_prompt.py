def create_prompt(
    destination,
    days,
    budget,
    travel_style,
    interests
):

    prompt = f"""
You are an expert travel planner.

Create a {days}-day itinerary.

Destination: {destination}
Budget: ₹{budget}
Travel Style: {travel_style}
Interests: {', '.join(interests)}


Include:

1. Day-wise plan
2. Morning, afternoon, evening activities
3. Hotel suggestions
4. Local foods to try
5. Estimated expenses
6. Travel tips

Use markdown formatting.
"""

    return prompt