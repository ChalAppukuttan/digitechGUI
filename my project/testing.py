import tkinter as tk
import random

# List of colors for the stroop test
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 60
return_count = 0  # variable to count the number of times return key is pressed
questions_left = 31


def endMenu():
    # Hide the game elements
    instructions.pack_forget()
    questionsLabel.pack_forget()
    timeLabel.pack_forget()
    label.pack_forget()
    e.pack_forget()
    startButton.pack_forget()

def startGame(event):
    global timeleft
    global questions_left
    global return_count  # variable needs to be global
    return_count += 1  # increase the count each time the function is called
    questions_left -= 1
    questionsLabel.config(text="Questions Left: " + str(questions_left) + "/30")
    if questions_left == -1 or 0:
        questions_left = questions_left * -1
        endMenu()
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

def startMenu():
    # Hide the game elements
    instructions.pack_forget()
    scoreLabel.pack_forget()
    questionsLabel.pack_forget()
    timeLabel.pack_forget()
    label.pack_forget()
    e.pack_forget()
    startButton.pack_forget()

    # Show the menu elements
    menuLabel.pack()
    playButton.pack()


def startGameFromMenu():
    # Hide the menu elements
    menuLabel.pack_forget()
    playButton.pack_forget()

    # Show the game elements
    instructions.pack()
    scoreLabel.pack()
    questionsLabel.pack()
    timeLabel.pack()
    label.pack()
    e.pack()
    startButton.pack()

    # Start the game
    startGame()

hydra = tk.Tk()
hydra.title("Stroop Test")
hydra.geometry("1820x1080")

instructions = tk.Label(hydra, text="Type in the color of the words, not the word text!", font=('Helvetica', 12))

scoreLabel = tk.Label(hydra, text="Press enter to start", font=('Helvetica', 12))

questionsLabel = tk.Label(hydra, text="Questions Left 30/30", font=('Helvetica', 12))

timeLabel = tk.Label(hydra, text="Time left: " + str(timeleft), font=('Helvetica', 12))

label = tk.Label(hydra, font=('Helvetica', 60))

e = tk.Entry(hydra)

startButton = tk.Button(hydra, text="Start Game", command=startGame)

menuLabel = tk.Label(hydra, text="Welcome to the Stroop Test Game!", font=('Helvetica', 30))

playButton = tk.Button(hydra, text="Play", command=startGameFromMenu)

# Start with the menu
startMenu()

hydra.bind('<Return>', startGame)

hydra.mainloop()

