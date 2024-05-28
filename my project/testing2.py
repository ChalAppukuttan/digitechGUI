import tkinter as tk  # Import the tkinter library for creating GUI applications
import random  # Import the random library for shuffling colors
import os  # Import the os library for file operations

# List of colors for the Stroop test
colors = ['Red', 'Blue', 'Green', 'Purple', 'Brown']
score = 0  # Initialize the score to 0
timeleft = 60  # Set the initial time left to 60 seconds
return_count = 0  # Variable to count the number of times the return key is pressed
questions_left = 30  # Number of questions to be answered

def write_score_to_file(score):
    """
    Write the score to a file called leaderboard.txt. If the file doesn't exist, create it.
    Append the score to the file.
    """
    filename = 'leaderboard.txt'

    # Check if file does not exist
    if not os.path.exists(filename):
        # Create the file
        open(filename, 'w').close()

    # Now write the score to the file
    with open(filename, 'a') as f:
        f.write(str(score) + '\n')

def endMenu():
    """
    End the game and display the leaderboard. Write the current score to the file.
    Hide the game elements and show the leaderboard with top 10 scores.
    """
    global score
    write_score_to_file(score)  # Save the score to the file
    # Hide game elements
    instructions.pack_forget()
    questionsLabel.pack_forget()
    timeLabel.pack_forget()
    label.pack_forget()
    e.destroy()
    startButton.pack_forget()

    filename = 'leaderboard.txt'

    # Check if file does not exist
    if not os.path.exists(filename):
        # Create the file
        open(filename, 'w').close()

    # Read scores from file and sort them in descending order
    with open(filename, 'r') as f:
        scores = [int(line.strip()) for line in f if line.strip() != '']
    scores.sort(reverse=True)

    # Create and display leaderboard label
    leaderboard_label = tk.Label(hydra, text="Leaderboard:", font=('Helvetica', 12))
    leaderboard_label.pack()

    # Display top 10 scores
    for i, score in enumerate(scores[:10]):
        score_label = tk.Label(hydra, text=f"{i + 1}#  {score}", font=('Helvetica', 12))
        score_label.pack()

def startGame(event):
    """
    Start the game. Initialize the countdown timer and display the next color.
    """
    global timeleft
    global questions_left
    global return_count  # variable needs to be global
    return_count += 1  # Increase the count each time the function is called
    questions_left -= 1
    questionsLabel.config(text="Questions Left: " + str(questions_left) + "/30")
    if questions_left == -1 or 0:
        questions_left = questions_left * -1
        endMenu()
    elif return_count == 30:
        timeleft = 0
    if timeleft == 60:
        countdown()
    nextColor()

def nextColor():
    """
    Display the next color. Check if the entered color is correct and update the score.
    Shuffle the colors and update the color text.
    """
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
    """
    Countdown timer for the game. Update the timer every second and stop when time runs out.
    """
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


def startMenu():
    """
    Display the start menu. Hide game elements and show menu elements.
    """
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
    d.pack()


def startGameFromMenu():
    """
    Start the game from the menu. Hide menu elements and show game elements.
    """
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


# Create the main application window
hydra = tk.Tk()
hydra.title("Stroop Test")  # Set the title of the window
hydra.geometry("1820x1080")  # Set the size of the window

# Create and configure labels and buttons
instructions = tk.Label(hydra, text="Type in the color of the word, not the word itself!", font=('Helvetica', 12))

scoreLabel = tk.Label(hydra, text="Press enter to start", font=('Helvetica', 12))

questionsLabel = tk.Label(hydra, text="Questions Left 30/30", font=('Helvetica', 12))

timeLabel = tk.Label(hydra, text="Time left: " + str(timeleft), font=('Helvetica', 12))

label = tk.Label(hydra, font=('Helvetica', 60))

e = tk.Entry(hydra)

d = tk.Entry(hydra)

startButton = tk.Button(hydra, text="Start Game", command=startGame)

menuLabel = tk.Label(hydra, text="Welcome to the Stroop Test Game!", font=('Helvetica', 30))

playButton = tk.Button(hydra, text="Play", command=startGameFromMenu)

# Start with the menu
startMenu()

# Bind the Return key to the startGame function
hydra.bind('<Return>', startGame)

# Run the main event loop
hydra.mainloop()
