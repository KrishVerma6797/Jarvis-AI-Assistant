from speak import speak
from dotenv import load_dotenv
import os
import requests

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            speak("City not found or something went wrong.")
            return

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        speak(f"The weather in {city} is currently {weather}.")
        speak(f"The temperature is {temp} degrees Celsius.")
        speak(f"The humidity is {humidity} percent.")

    except Exception as e:
        print("[DEBUG] Weather error:", e)
        speak("I couldn't fetch the weather at the moment.")
