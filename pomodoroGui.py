from tkinter import *
import pygame


def countdown(count=25*60):
    # change text in label
    time_str = time_string(count)
    countdown_label['text'] = time_str

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    if count <= 0:
        play()

def onClick():
    if countdown_label['text'] != initial_text:
        return
    else:
        countdown(25*60)

def time_string(seconds:int) -> str:

    m = seconds // 60
    s = seconds % 60

    time_str = ""

    if m < 10:
        time_str += "0"
    time_str += str(m)+":"

    if s < 10:
        time_str += "0"
    time_str += str(s)

    return time_str

pygame.mixer.init() # initialise the pygame

def play():
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play(loops=0)

root = Tk()
root.title('Pomodoro')
root.geometry("350x350")
root.config(bg="black")

initial_text = "Press"

# Label
countdown_label = Label(
    root,
    text= initial_text,
    font=("Helvetica", 48),
    fg="green",
    bg="black"
)

countdown_label.pack(
    pady=20
)

start_button = Button(
    root, 
    bg="green",
    width= 10,
    height= 2,
    command=onClick
    )
start_button.pack(

    pady= 80
)

root.mainloop()

