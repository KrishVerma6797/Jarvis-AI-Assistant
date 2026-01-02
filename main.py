from system_info import *
from prettytable import PrettyTable
from wish import wishMe
import wolframalpha
from takeCommand import takeCommand
from speak import speak
import random
import webbrowser
import wikipedia
import pywhatkit
import datetime
from weather import get_weather
from news import get_news
import pyjokes
import os
from llama_cpp import Llama
from llama import*
from load import*
from app_scanner import find_app_path



wolfram_app_id = os.getenv("WOLFRAM_APP_ID")

def run_jarvis():
    client = wolframalpha.Client(wolfram_app_id)

    while True:
        query = takeCommand()      # query is the variable that take all the command that i speak

        if query == "none":      # if it hears nothing or i speak nothing then it continue
            continue

        # Trigger response when user says 'jarvis' or 'r jarvis'
        if 'jarvis' in query or 'r jarvis' in query:       # it starts or gets trigger if i say jarvis or r jarvis  and rreply to which yes i m her, tell me , yes? etc...
            responses = ["Yes?", "I'm here.", "At your service.", "Tell me."]
            speak(random.choice(responses))
            continue


        elif 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            try:
                result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)   
                speak(result)
          
            except:
                speak("No results found on Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open facebook' in query:
            webbrowser.open("https://facebook.com")

        elif 'open linkedin' in query:
            webbrowser.open("https://linkedin.com")

        elif 'play song' in query:
            song = query.replace('play song', '')      # replace the word"play song from query to extract actual song 
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'time' in query:
            time = datetime.now().strftime("%H:%M")  # give in fourmat of hour:minutes
            speak(f"The time is {time}")
            

        elif 'date' in query:
            date =datetime.now().strftime("%A ,%B %d, %Y")     # day:month:date:year
            speak(f"Today is {date}")
         

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)


        elif "where is" in query and "installed" in query:
            app_name = query.replace("where is", "").replace("installed", "").strip()
            response = find_app_path(app_name)
            print("🧠", response)
            speak(response)


        elif 'news' in query:
            get_news()


        elif "system info" in query or "my system" in query:
            tell_system_info()


        elif 'weather' in query:
            speak("For which city would you like the weather information?")
            city = takeCommand()
            if city != "none":
                get_weather(city)


        elif 'who is' in query or 'what is' in query:
            try:
                res = client.query(query)
                answer = next(res.results).text
                speak(answer)
            except:
                try:
                    speak("Let me check on Wikipedia.")
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except:
                    speak("Sorry, I couldn't find anything.")

        elif any(word in query for word in ['exit', 'stop', 'quit', 'close']):
            speak("Goodbye! Have a nice day.") 
            break



        else:
            reply = ask_llama(query)
            print("LLaMA 3:", reply)  # <-- show full text in terminal
            speak(reply)              # <-- speak it out loud

        

#----------- Run Jarvis ------------
if __name__ == "__main__":    # Runs the Jarvis assistant only if this script is executed directly (not imported)
    try:
        run_jarvis()
    except KeyboardInterrupt:
        speak("Shutting down. Goodbye.")
        
