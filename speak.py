import pyttsx3

def speak(text):
    if not text or len(text.strip()) < 2:
        return

    if any(x in text.lower() for x in ["<end_of_turn>", "start_of_turn"]):
        return

    try:
        print(text)
        engine = pyttsx3.init()   # 🔥 recreate engine every time
        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print("TTS error:", e)
