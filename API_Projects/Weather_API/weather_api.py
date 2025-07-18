import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not API_KEY:
        print("🚫 API key not found. Check your .env file.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print(f"\n📍 Weather in {city.title()}")
            print("📝 Description:", data["weather"][0]["description"])
            print("🌡️ Temperature:", data["main"]["temp"], "°C")
            print("💧 Humidity:", data["main"]["humidity"], "%")
            print("💨 Wind Speed:", data["wind"]["speed"], "m/s")
        elif response.status_code == 404:
            print(f"❌ City '{city}' not found. Please try again.")
        elif response.status_code == 401:
            print("🔐 Invalid API key. Please check your .env file.")
        else:
            print("⚠️ Unexpected error:", data.get("message", "Unknown error"))

    except requests.exceptions.RequestException as e:
        print("🚫 Network or connection error:", e)

# Main loop
while True:
    city = input("\nEnter a city name (or 'exit' to quit): ").strip()
    if city.lower() == "exit":
        print("👋 Goodbye!")
        break
    elif city == "":
        print("⚠️ City name cannot be empty.")
    else:
        get_weather(city)