import tkinter as tk
import random

# List of colors for the stroop test
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 60
return_count = 0  # variable to count the number of times return key is pressed
questions_left = 30

def startGame(event):
    global timeleft
    global return_count  # variable needs to be global
    return_count += 1  # increase the count each time the function is called
    if return_count == 30:
        timeleft = 0
    if timeleft == 60:
        countdown()
    nextColor()


def nextColor():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0, tk.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


hydra = tk.Tk()
hydra.title("Stroop Test")
hydra.geometry("1820x1080")

instructions = tk.Label(hydra, text="Type in the color of the words, not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tk.Label(hydra, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tk.Label(hydra, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tk.Label(hydra, font=('Helvetica', 60))
label.pack()

e = tk.Entry(hydra)
e.pack()
e.focus_set()

hydra.bind('<Return>', startGame)

hydra.mainloop()

