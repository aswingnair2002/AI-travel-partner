# ✈️ AI Travel Planner

AI Travel Planner is a web application that helps users create personalized travel itineraries using AI. The app considers factors like budget, travel style, interests, and current weather conditions to suggest a complete travel plan.

It also shows destination images and provides quick access to Google Maps for exploring places to visit.

---

##  Features

- Generate AI-powered travel itineraries using Google Gemini
- Get real-time weather information
- View beautiful destination images using Pexels
- Open recommended places directly in Google Maps
- Plan trips based on budget and interests
- Support for different travel styles like solo, family, adventure, and luxury travel

---

##  Technologies Used

- Python
- Streamlit
- Google Gemini API
- OpenWeather API
- Pexels API
- Google Maps

---

##  Project Structure

```text
AI-travel-planner/

├── app.py
├── requirements.txt
├── .env

├── prompts/
│   └── itinerary_prompt.py

├── services/
│   ├── gemini_service.py
│   ├── weather_service.py
│   ├── image_service.py
│   └── maps_service.py
```

---

## ⚙️ How to Run

Clone the repository:

```bash
git clone https://github.com/aswingnair2002/AI-travel-partner.git
```

Move into the project folder:

```bash
cd AI-travel-partner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_openweather_api_key
PEXELS_API_KEY=your_pexels_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Improvements

Some features I would like to add in the future:

- Flight recommendations
- Hotel suggestions
- Seasonal and off-season travel analysis
- Festival and event information
- Currency conversion for international trips
- Interactive maps with markers
- Download itinerary as PDF
- Save previous travel plans

---

##  About Me

I'm an MCA graduate (2025) who enjoys building AI-based applications and exploring new technologies. This project was developed as a hackathon project to combine generative AI with real-world travel planning.

---

## If you like this project

Feel free to fork the repository, raise issues, or suggest improvements!