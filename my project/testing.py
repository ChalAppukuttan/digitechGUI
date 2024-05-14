import tkinter as tk
import random
import os

# List of colors for the stroop test
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 60
return_count = 0  # variable to count the number of times return key is pressed
questions_left = 30


def write_score_to_file(score):
    filename = 'leaderboard.txt'

    # Check if file does not exist
    if not os.path.exists(filename):
        # Create the file
        open(filename, 'w').close()

    # Now write the score to the file
    with open(filename, 'a') as f:
        f.write(str(score) + '\n')


def endMenu():
    global score
    # Hide the game elements
    write_score_to_file(score)
    instructions.pack_forget()
    questionsLabel.pack_forget()
    timeLabel.pack_forget()
    label.pack_forget()
    e.pack_forget()
    startButton.pack_forget()

    filename = 'leaderboard.txt'

    # Check if file does not exist
    if not os.path.exists(filename):
        # Create the file
        open(filename, 'w').close()

    # Now read scores from file and sort them in descending order
    with open(filename, 'r') as f:
        scores = [int(line.strip()) for line in f if line.strip() != '']
    scores.sort(reverse=True)

    # Create leaderboard label
    leaderboard_label = tk.Label(hydra, text="Leaderboard:", font=('Helvetica', 12))
    leaderboard_label.pack()

    # Display top 10 scores
    for i, score in enumerate(scores[:10]):
        score_label = tk.Label(hydra, text=f"{i + 1}. {score}", font=('Helvetica', 12))
        score_label.pack()



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

