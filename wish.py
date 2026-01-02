import pyttsx3
from datetime import datetime
from speak import speak
def wishMe():
    hour = int(datetime.now().hour)     # gets current hour(0-23 format)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
  
    speak("I am Jarvis. How can I assist you today?")
    

