from win32com.client import Dispatch
say=Dispatch("SAPI.Spvoice")
str="Hey there! How are you ? What's going on there ?"
say.Speak(str)