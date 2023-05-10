from tkinter import *
import time

def countdown(count):
    # change text in label
    time_str = time_string(count)
    countdown_label['text'] = time_str

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

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

root = Tk()
root.title('Pomodoro')
root.geometry("600x400")


# Label
countdown_label = Label(
    root, 
    text="", 
    font=("Helvetica", 48),
    fg="green",
    bg="black"
)

countdown_label.pack(
    pady=20
)

countdown(25*60)
root.mainloop()

