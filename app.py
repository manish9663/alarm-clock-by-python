from datetime import datetime
from playsound import playsound
from tkinter import *
master = Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
    alarm_time = e.get()
    alarm_hour=alarm_time[0:2]
    alarm_minute=alarm_time[3:5]
    alarm_second=alarm_time[6:8]
    alarm_period=alarm_time[9:11].upper()
    print(alarm_time)
    print("setting up alarm..")
    while True:
        now = datetime.now()
        current_hour=now.strftime("%I")
        current_minute=now.strftime("%M")
        current_second=now.strftime("%S")
        current_period=now.strftime("%p")
        #print(current_second)
        if(alarm_period==current_period):
            if(alarm_hour==current_hour):
                if(alarm_minute==current_minute):
                    if(alarm_second==current_second):
                        print("walk up!")
                        playsound('tone.mp3')
                        break

b = Button(master, text = "set alarm", width = 10, command = callback, activeforeground= 'black')
b.pack()

mainloop()

