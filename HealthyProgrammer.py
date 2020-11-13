from pygame import mixer
from datetime import datetime
import time

def music_for_activity(song_name):
    
    mixer.init()
    mixer.music.load(song_name)
    mixer.music.play()

def set_file(str):
    with open("activity.txt",'a') as f:
        f.write(f"{str} {datetime.now()}\n")
        

if __name__=="__main__":
    water_time=time.time()
    eyes_time=time.time()
    physical_time=time.time()
    water_secs=10
    eyes_secs=15
    physical_secs=20
    while True:
        if time.time()-water_time>water_secs:
            water=music_for_activity("water.mp3")
            water_time=time.time()
            for_water=input("Water drinking time\nEnter drank to stop ")
            water_text="You drank water at"
            water_file=set_file(water_text)
            if for_water=="drank":
                mixer.music.stop()
            

        if time.time()-eyes_time>eyes_secs:
            eyes=music_for_activity("eyes.mp3")
            eyes_time=time.time()
            for_eyes=input("Eyes exercise time\nEnter done to stop ")
            eyes_text="You did eyes exercise at"
            eyes_file=set_file(eyes_text)
            if for_eyes=="done":
                mixer.music.stop()
            

        if time.time()-physical_time>physical_secs:
            physical=music_for_activity("physical.mp3")
            physical_time=time.time()
            for_physical=input("Physical exercise time\nEnter pydone to stop ")
            physical_text="You did physical exercise at"
            physical_file=set_file(physical_text)
            if for_physical=="pydone":
                mixer.music.stop()
            
            


    
