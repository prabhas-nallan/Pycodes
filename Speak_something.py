from win32com.client import Dispatch
def say(str):
    tell=Dispatch("SAPI.Spvoice")
    tell.Speak(str)

if __name__ == "__main__":
    s="Yeh kya baath hui.."
    say(s)