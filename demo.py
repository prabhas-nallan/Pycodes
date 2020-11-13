from win32com.client import Dispatch
import speech_recognition as sr
from  translate import Translator
def speak(s):
    say=Dispatch("SAPI.Spvoice")
    say.Speak(s)
def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=3500
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language="en")
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    query=takeCommand().lower()
    if 'translator' in query:
            speak("The available languages are Telugu , Italian , French , Arabic")
            r1=sr.Recognizer()
            with sr.Microphone() as source2:
                print("Choose the language...")
                # speak("Choose the language")
                r1.energy_threshold=3500
                r1.pause_threshold=0.8
                audio1=r1.listen(source2)
            try:
                print('Recognizing language...')
                say=r1.recognize_google(audio1,language="en")
                print(f"You spoke: {say}\n")

                if "Telugu" in say:
                    speak("Say something to translate in Telugu")
                    r3=sr.Recognizer()
                    with sr.Microphone() as source3:
                        print("Listening to translate in to Telugu...")
                        r3.energy_threshold=3500
                        r3.pause_threshold=0.8
                        audio3=r3.listen(source3)
                    try:
                        print('Recognizing to translate in to Telugu...')
                        say2=r3.recognize_google(audio3,language="en")
                        print(f"User Said: {say2}\n")
                        trans=Translator(to_lang="Telugu")
                        translation=trans.translate(say2)
                        print(translation)
                        speak(translation)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
