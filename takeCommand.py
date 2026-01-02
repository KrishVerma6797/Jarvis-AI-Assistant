from speak import speak
import speech_recognition as sr
#---------giving command by sayting it function------------------
def takeCommand():
    r = sr.Recognizer()         #creates a recognizer
    with sr.Microphone() as source:      #use mic to listen
        print("Listening...")
        r.pause_threshold = 1             # wait for 1sec of silence to stop listening

         # ✅ This line does the noise cancellation magic
        r.adjust_for_ambient_noise(source, duration=1)  # listen 1 sec to noise & calibrate

        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)                # record audio (start in 5s,max speed 8s)
        except:
            speak("Microphone not working properly.")        # if mic fails: say microphone not working
            return "none"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')        # try to recognize using google(indian english)
        print(f"You said: {query}")
        return query.lower()       # if success print in lower case
    except:
        speak("Sorry, I didn't catch that.")      # if fails print didnt heard or catch or whatsoever
        return "none"

