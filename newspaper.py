from win32com.client import Dispatch
import requests
import json

def speak(String):
    say=Dispatch("SAPI.Spvoice")
    say.Speak(String)
if __name__ == "__main__":
    speak("Let's begin the news")
    url="http://newsapi.org/v2/top-headlines?country=us&apiKey=92f1f81f65ce441ab89108e92a93208d"
    news=requests.get(url)
    news_text=news.text
    news_dict=json.loads(news_text)
    arts=news_dict["articles"]
    for tiltle in arts:
        speak(tiltle["title"])
    speak("Thank you")