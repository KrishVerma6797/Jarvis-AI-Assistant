from speak import speak
from dotenv import load_dotenv
import requests
import os
load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")

def get_news():
    speak("Here are the top news headlines.")
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}" # Creates news api url  and country=us sets news source from usa and news_api_key is variable that contian api key string

    try:
        response = requests.get(url)       # send an http get request to news api to get some data
        print(f"[DEBUG] Status Code: {response.status_code}")    # send an http get request to news api to get some data#prints http respnse status code
        print(f"[DEBUG] Raw Response: {response.text[:200]}")    # prints first 200 characters of raw respnse for debugging

        if response.status_code != 200:    # if api didnt return status 200 ok then it print error
            speak("News API returned an error.")
            return

        data = response.json()     #parses raw json response into python dictionary i.e. data

        if "articles" not in data or not data["articles"]:    # if article key is missing or it is empty then it notifies use and exit funnction
            speak("There are no news articles available right now.")
            return

        articles = data["articles"][:5]   # pick top 5 news articles 
        for i, article in enumerate(articles, start=1):
            title = article.get('title', 'No title available')
            print(f"[DEBUG] News {i}: {title}")    # extract the title and prints
            speak(f"News {i}: {title}")
    except Exception as e:
        print("[DEBUG] News error:", e)
        speak("Unable to fetch news at the moment.")

