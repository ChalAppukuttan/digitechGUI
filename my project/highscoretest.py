import tkinter as tk
import random

# List of colors for the Stroop test
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 60
high_scores = []
enter_number = 0

try:
    with open('high_scores.txt', 'r') as f:
        high_scores = [int(line.strip()) for line in f]
except FileNotFoundError:
    pass

def startGame(event):
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
    else:
        # Game over, save high score
        high_scores.append(score)
        high_scores.sort(reverse=True)
        with open('high_scores.txt', 'w') as f:
            for s in high_scores[:10]:  # Save only top 10 scores
                f.write(str(s) + '\n')


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
hydra.bind('<Return>', startGame)
e.pack()
e.focus_set()
hydra.mainloop()

