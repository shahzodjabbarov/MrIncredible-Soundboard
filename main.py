
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import *
import pygame

root = Tk()
root.geometry("650x600")
root.title("Mr Incredible Meme")
pygame.mixer.init()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



filename=PhotoImage(file=relative_to_assets("back1.png"))
background_label=Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

def first():
   pygame.mixer.music.load(relative_to_assets("first.mp3"))
   pygame.mixer.music.play()
image_1 = PhotoImage(file=(relative_to_assets("button_1.png")))
button_1 = Button(root, image=image_1, command=lambda:first()).place(x=45.0,y=27.0,width=100.0,height=100.0)

def second():
   pygame.mixer.music.load(relative_to_assets("second.mp3"))
   pygame.mixer.music.play()
image_2 = PhotoImage(file=(relative_to_assets("button_2.png")))
button_2 = Button(image=image_2, command=lambda:second()).place(x=200.0,y=27.0,width=100.0,height=100.0)

def third():
   pygame.mixer.music.load(relative_to_assets("third.mp3"))
   pygame.mixer.music.play()
image_3 = PhotoImage(file=(relative_to_assets("button_3.png")))
button_3 = Button(image=image_3, command=lambda:third()).place(x=347.0,y=27.0,width=100.0,height=100.0)

def fourth():
   pygame.mixer.music.load(relative_to_assets("fourth.mp3"))
   pygame.mixer.music.play()
image_4 = PhotoImage(file=(relative_to_assets("button_4.png")))
button_4 = Button(image=image_4, command=lambda:fourth()).place(x=503.0,y=27.0,width=100.0,height=100.0)

def fifth():
   pygame.mixer.music.load(relative_to_assets("fifth.mp3"))
   pygame.mixer.music.play()
image_5 = PhotoImage(file=(relative_to_assets("button_5.png")))
button_5 = Button(image=image_5, command=lambda:fifth()).place(x=43.0,y=169.0,width=100.0,height=100.0)

def sixth():
   pygame.mixer.music.load(relative_to_assets("sixth.mp3"))
   pygame.mixer.music.play()
image_6 = PhotoImage(file=(relative_to_assets("button_6.png")))
button_6 = Button(image=image_6, command=lambda:sixth()).place(x=200.0,y=169.0,width=100.0,height=100.0)

def seventh():
   pygame.mixer.music.load(relative_to_assets("seventh.mp3"))
   pygame.mixer.music.play()
image_7 = PhotoImage(file=(relative_to_assets("button_7.png")))
button_7 = Button(image=image_7, command=lambda:seventh()).place(x=346.0,y=169.0,width=100.0,height=100.0)

def eighth():
   pygame.mixer.music.load(relative_to_assets("eighth.mp3"))
   pygame.mixer.music.play()
image_8 = PhotoImage(file=(relative_to_assets("button_8.png")))
button_8 = Button(image=image_8, command=lambda:eighth()).place(x=503.0,y=169.0,width=100.0,height=100.0)

def nineth():
   pygame.mixer.music.load(relative_to_assets("nineth.mp3"))
   pygame.mixer.music.play()
image_9 = PhotoImage(file=(relative_to_assets("button_9.png")))
button_9 = Button(image=image_9, command=lambda:nineth()).place(x=45.0,y=320.0,width=100.0,height=100.0)

def tenth():
   pygame.mixer.music.load(relative_to_assets("tenth.mp3"))
   pygame.mixer.music.play()
image_10 = PhotoImage(file=(relative_to_assets("button_10.png")))
button_10 = Button(image=image_10, command=lambda:tenth()).place(x=200.0,y=320.0,width=100.0,height=100.0)

def eleventh():
   pygame.mixer.music.load(relative_to_assets("eleventh.mp3"))
   pygame.mixer.music.play()
image_11 = PhotoImage(file=(relative_to_assets("button_11.png")))
button_11 = Button(image=image_11, command=lambda:eleventh()).place(x=345.0,y=320.0,width=100.0,height=100.0)

def twelveth():
   pygame.mixer.music.load(relative_to_assets("twelveth.mp3"))
   pygame.mixer.music.play()
image_12 = PhotoImage(file=(relative_to_assets("button_12.png")))
button_12 = Button(image=image_12, command=lambda:twelveth()).place(x=503.0,y=320.0,width=100.0,height=100.0)

def thirteenth():
   pygame.mixer.music.load(relative_to_assets("thirteenth.mp3"))
   pygame.mixer.music.play()
image_13 = PhotoImage(file=(relative_to_assets("button_13.png")))
button_13 = Button(image=image_13, command=lambda:thirteenth()).place(x=45.0,y=450.0,width=100.0,height=100.0)

def fourteens():
   pygame.mixer.music.load(relative_to_assets("fourteens.mp3"))
   pygame.mixer.music.play()
image_14 = PhotoImage(file=(relative_to_assets("button_14.png")))
button_14 = Button(image=image_14, command=lambda:fourteens()).place(x=200.0,y=450.0,width=100.0,height=100.0)

def fifteenth():
   pygame.mixer.music.load(relative_to_assets("fifteenth.mp3"))
   pygame.mixer.music.play()
image_15 = PhotoImage(file=(relative_to_assets("button_15.png")))
button_15 = Button(image=image_15, command=lambda:fifteenth()).place(x=345.0,y=450.0,width=100.0,height=100.0)

def sixteenth():
   pygame.mixer.music.load(relative_to_assets("sixteenth.mp3"))
   pygame.mixer.music.play()
image_16 = PhotoImage(file=(relative_to_assets("button_16.png")))
button_16 = Button(image=image_16, command=lambda:sixteenth()).place(x=504.0,y=450.0,width=100.0,height=100.0)

root.resizable(False, False)
root.mainloop()
