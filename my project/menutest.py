import random
import tkinter as tk

# List of colors for the Stroop test
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 60


def menu():
    menu_window = tk.Toplevel(hydra)
    menu_window.title("Menu")

    start_button = tk.Button(menu_window, text="Start Game", command=startGame)
    start_button.pack()

    # Add more buttons as needed
    # quit_button = tk.Button(menu_window, text="Quit Game", command=hydra.destroy)
    # quit_button.pack()


def startGame(event=None):
    if timeleft == 60:
        countdown()
    nextColor()
    if event is not None:
        event.widget.master.destroy()  # Add this line



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
hydra.withdraw()
menu()
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
hydra.bind('<Return>', startGame)
e.pack()
e.focus_set()
hydra.mainloop()

