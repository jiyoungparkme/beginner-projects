# music player with tkinter and pygame
from tkinter import *
import sys
import os
from pygame import *
from pygame.locals import QUIT

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root = Tk()
root.title("Music player")

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

# playlist
playlist = Listbox(root, selectmode=SINGLE, bg="DodgerBlue2", fg="white", font=("arial", 15), width=30 )
playlist.grid(columnspan=5)
os.chdir(r"C:\Users\zeear\Desktop\지영\여행\영상\노래")
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn = Button(root, text='play', command=playsong)
playbtn.config(font=("arial" ,20),fg="purple", padx=4, pady=4)
playbtn.grid(row=1 , column=0)

playbtn = Button(root, text='pause', command=pausesong)
playbtn.config(font=("arial" ,20),fg="purple", padx=7, pady=7)
playbtn.grid(row=1 , column=1)

playbtn = Button(root, text='stop', command=stopsong)
playbtn.config(font=("arial" ,20),fg="purple", padx=7, pady=7)
playbtn.grid(row=1 , column=2)

playbtn = Button(root, text='resume', command=resumesong)
playbtn.config(font=("arial" ,20),fg="purple", padx=7, pady=7)
playbtn.grid(row=1 , column=3)

mainloop()




# pygame.init()

# # music player screen option set
# size = [500, 400]
# screen = pygame.display.set_mode(size)

# title = "My Music Player"
# pygame.display.set_caption(title)

# # Setting for music player inside
# clock = pygame.time.Clock()
# color = (0,0,0)

# # main event

# SB = 0
# while SB==0:
#     screen.fill((255,255,255))

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             SB = 1
            
#         else:
#             screen.fill(color)
#         pygame.display.flip()
# pygame.quit()
# sys.exit()

