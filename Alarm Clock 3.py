from tkinter import *
import datetime
import time
import sys
import winsound
from tkinter import messagebox
import random 
import pygame
from tkinter import filedialog

clock = Tk()
clock.title("Alarm Clock 2021")
clock.geometry("500x250")

pygame.mixer.init()

#----------------------------------------------------------------------------------------------------

#This is for the output message when the alarm rings
def abusive():
    the_list = {
        1: "Your mother's breasts sag with such severity that the late, great surrealist artist Salvador Dali mistook them for clocks",
        2: "I'm gonna plant a tree in your mom's ass and then fuck your sister in its shade.",
        3: "You are the reason they put instructions on shampoo.",
        4: "Your ass is grass and I've got the weed-whacker." ,
        5: "You'd have better luck trying to score with your sister.",
        6: "I used to fuck guys like you in prison",
        7: "You're entitled to your opinion, but your opinion is wrong.",
        8: "Did you think this was going to be easy. NO!!!!!!!!! SO GET YOUR ASS UP AND START WORKING "
        }
    number = random.randint(1,8)
    return the_list[number]


#-----------------------------------------------------------------------------------------------------


#These two functions are used to make the alarm 
def alarm(clock):
    try: 
        #here is where an error message will pop up if the time is not inputted
        if hour.get()=="" or min.get()=="" or sec.get()=="":
            messagebox.showinfo("Information Error","""
            Informative message
            You have inputed the time incorrectly""")
        
        #here is where an error message will pop up if the time is inputted incorectly
        elif len(hour.get()) == 1 or len(min.get())==1 or len(sec.get())==1:
            messagebox.showerror("Input Error", """
            Input the time in 24 hr format
            Make sure there is always two digits for each entry
            """)
      
        #here is where we compare the actual time to the alarm we set
        else:
            while True:
                current_time = datetime.datetime.now()
                time = current_time.strftime("%H:%M:%S")
                print(time)
                if time == clock:
                    pygame.mixer.music.load(new_filepath)
                    pygame.mixer.music.play(loops=3)
                    messagebox.showerror("WAKE UP", abusive())
                    break
    except:
        messagebox.showerror("ERROR","UNKNOWN ERROR")

def set_timer():
    clock = f"{hour.get()}:{min.get()}:{sec.get()}" 
    alarm(clock)

#--------------------------------------------------------------------------------------------------

#display the time 
def get_time():
    timeVar = time.strftime("%H:%M:%S %p")
    thisTime.config(text = timeVar)
    thisTime.after(200, get_time)

thisTime = Label(clock, font=("Calibri", 25), bg = "black", fg = "white")
thisTime.pack()
get_time()

#-----------------------------------------------------------------------------------------------------
#displays a box to choose your song

new_filepath = ""
def openfile():
    global new_filepath
    filepath =filedialog.askopenfilename(title = "Choose Music File", filetypes=(("music files","*.mp3"), ("all files", "*.*")))
    for letter in filepath:
        if letter  == "/":
            new_filepath +=letter +"/"
        else: 
            new_filepath+=letter
    
    songTitle = ""
    for letter in new_filepath[::-1]:
        if letter == "/":
            break
        else: 
            songTitle+=letter
    songTitle= songTitle[::-1]
    the_song = Label(clock, text = songTitle, font = ("Arial", "10")).place(x = 190, y =200)
    return new_filepath




#-----------------------------------------------------------------------------------------------------
def stopPLaying():
    pygame.mixer.music.stop()
#-----------------------------------------------------------------------------------------------------


hour = StringVar()
min =StringVar()
sec = StringVar()

#The labels
add_hour = Label(clock, text = "Hour", font = "Arial").place(x=110, y=60)
add_min = Label(clock, text = "Min", font = "Arial").place(x=150, y= 60)
add_sec = Label(clock, text = "Sec", font = "Arial").place(x=190, y=60)
add_song = Label(clock, text = "Choose a Song", font="Arial").place (x = 70, y = 170)


#The entry's
hourTime = Entry(clock, textvariable=hour , width = "5").place(x=110, y = 90)
minTime = Entry(clock, textvariable=min ,  width = "5").place(x=150, y = 90)
secTime = Entry(clock, textvariable=sec ,  width = "5").place(x=190, y =90)

#The Buttons
submit = Button(clock, text = "Set Alarm", fg = "red", font = "Arial",  command=set_timer).place(x= 110, y = 120)
songFile = Button(clock, text = "Choose File", width ="20", command= openfile).place(x = 190, y= 170)
stopping = Button(clock, text = "Stop Playing", fg = "red", font = "Arial",  command=stopPLaying).place(x= 200, y = 120)
clock.mainloop()