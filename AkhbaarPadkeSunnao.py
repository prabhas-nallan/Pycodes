import json
import requests
from win32com.client import Dispatch
def speak(str):
    say=Dispatch("SAPI.Spvoice")
    say.Speak(str)

if __name__=="__main__":
    speak("Lets begin")
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=92f1f81f65ce441ab89108e92a93208d"
    news=requests.get(url).text
    news_dict=json.loads(news)
    articles=(news_dict["articles"])

    for article in articles:
        speak(article["description"])
    speak("Thanks for listening")