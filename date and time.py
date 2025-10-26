from tkinter import *
from time import *

# -------------Machanisam-------------

def update():
    time_string = strftime("%I:%M:%S|%p")
    time_label.config(text=time_string)
    time_label.after(1000, update)

    day_string = strftime("%A")
    day_label.config(text=day_string)
    
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

# -------------Display-------------

window = Tk()
window.title("Digital Clock")
window.config(bg="#211832")

# -------------Time-------------

time_label = Label(window, font=("courier", 50, "bold"), fg="#B95E82", bg="#211832")
time_label.pack()

# -------------Day-------------

day_label = Label(window, font=("Roboto", 25, "bold"), fg="#B95E82", bg="#211832")
day_label.pack()

# -------------Date-------------

date_label = Label(window, font=("Ink Free", 50, "bold"), fg="#B95E82", bg="#211832")
date_label.pack()


update()
window.mainloop()