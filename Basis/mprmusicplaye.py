import os
import webbrowser
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import winsound
import pickle
import pygame


root = Tk()
root.title("Player")
frame1 = Frame(root)
menu = Menu(frame1)
root.config(menu=menu)


root.filename = ""
root.playlist = []
root.pauseFlag = False
root.songAdded = False
root.i = 0


def openFile():
    try:
        root.songAdded = True
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select your cool music track", filetypes=(
        ("mp3 Music Files", "*.mp3"), ("m4a Music Files", "*.m4a")))
        root.playlist.append(root.filename)
        print(" Added " + root.filename)
        root.screenMessage.set("Good! Now Press on the Play Button")
    except:
        print("Cannot load the music")








def playMusic():
    if (root.songAdded == False):
        root.screenMessage.set("First add some Music man!")
    else:
        try:
            if (root.pauseFlag == True):
                pygame.mixer.music.unpause()
            else:
                print("Playing")
                pygame.mixer.init()
                pygame.mixer.music.load(root.playlist[root.i])
                pygame.mixer.music.play()
                root.screenMessage.set("Playing " + root.playlist[root.i])
        except:
            print("Could not play the music")


def pauseMusic():
    if (root.songAdded == False):
        root.screenMessage.set("First add some Music man!")
    else:
        try:
            pygame.mixer.music.pause()
            root.pauseFlag = True
            root.screenMessage.set("Paused")
        except:
            print("Cannot Pause the Music")


def stopMusic():
    if (root.songAdded == False):
        root.screenMessage.set("First add some Music man!")
    else:
        pygame.mixer.music.fadeout(600)
        root.screenMessage.set("End of Playback!")


def prevMusic():
    if (root.songAdded == False):
        root.screenMessage.set("First add some Music man!")
    else:
        try:
            if (root.playlist[root.i - 1]):
                root.i -= 1
                playMusic()
            else:
                print("No previous songs")
                root.screenMessage.set("No previous songs")
        except:
            stopMusic()
            print("No previous songs")


def nextMusic():
    if (root.songAdded == False):
        root.screenMessage.set("First add some Music man!")
    else:
        try:

            if (root.playlist[root.i]):
                root.i += 1
                playMusic()
            else:
                root.i -= 1
        except:
            root.screenMessage.set("End of Playback, Please add more songs")


def end():
    exit()







subMenu = Menu(menu)
menu.add_cascade(label="Media", menu=subMenu)
subMenu.add_command(label="Open File", command=openFile)
subMenu.add_separator()

subMenu.add_separator()
subMenu.add_command(label="exit", command=exit)




one = Label(root, text="Welcome", bg="light blue", fg="black")
one.pack(fill=X)
two = Label(root, text="To DJNR Music Player", bg="white", fg="blue")
two.pack(fill=X)
three = Label(root, text="Created By DJNR", bg="pink", fg="black")
three.pack(fill=X)

topFrame = Frame(root)  # definig a frame that will contain the Widgets
topFrame.pack()
bottomFrame = Frame(root)  # Similarly, definging the next Frame
bottomFrame.pack(side=BOTTOM)



button1 = Button(topFrame, text="Previous", fg="red",
                 command=prevMusic)  # Positioning Button as (<FrameName>,<Text to Appear>,<Text Color>)
button1.pack(side=LEFT, padx=5, pady=20)
button2 = Button(topFrame, text="Play", fg="green", command=playMusic)
button2.pack(side=LEFT, padx=5, pady=20)
button3 = Button(topFrame, text="Pause", fg="black", command=pauseMusic)
button3.pack(side=LEFT, padx=5, pady=20)
button5 = Button(topFrame, text="Stop", fg="red", command=stopMusic)
button5.pack(side=LEFT, padx=5, pady=20)
button4 = Button(topFrame, text="Next", fg="blue", command=nextMusic)
button4.pack(side=LEFT, padx=5, pady=20)


root.screenMessage = StringVar()
label = Message(root, textvariable=root.screenMessage, relief=RAISED)
root.screenMessage.set("Welcome, to DJNR Music Player")
label.pack(side=BOTTOM, fill=X)
root.mainloop()