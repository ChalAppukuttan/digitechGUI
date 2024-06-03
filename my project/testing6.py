import tkinter as tk
import random

class StroopTestGame:
    def __init__(self, master):
        """Initialize the game with the main Tkinter window and game variables."""
        self.master = master
        # List of colors to be used in the game
        self.colors = ['Red', 'Blue', 'Green', 'Purple', 'Brown']
        # Initial game state variables
        self.score = 0
        self.timeleft = 60
        self.questions_left = 30
        self.return_count = 0

        # Setup the GUI widgets
        self.setup_widgets()
        # Display the start menu
        self.start_menu()

    def setup_widgets(self):
        """Setup the initial GUI widgets."""
        # Instructions for the user
        self.instructions = tk.Label(self.master, text="Type in the color of the words!", font=('Helvetica', 12))
        # Label to display the score
        self.scoreLabel = tk.Label(self.master, text="Press enter to start", font=('Helvetica', 12))
        # Label to display the number of questions left
        self.questionsLabel = tk.Label(self.master, text="Questions Left: 30/30", font=('Helvetica', 12))
        # Label to display the remaining time
        self.timeLabel = tk.Label(self.master, text=f"Time left: {self.timeleft}", font=('Helvetica', 12))
        # Label to display the color words
        self.label = tk.Label(self.master, font=('Helvetica', 60))
        # Entry widget for user input
        self.e = tk.Entry(self.master)
        # Button to start the game
        self.startButton = tk.Button(self.master, text="Start Game", command=self.start_game)
        # Label for the menu
        self.menuLabel = tk.Label(self.master, text="Welcome to the Stroop Test Game!", font=('Helvetica', 30))
        # Button to play the game from the menu
        self.playButton = tk.Button(self.master, text="Play", font=200, command=self.start_game_from_menu)
        # Back button from the game menu
        self.backButton = tk.Button(self.master, text="Back", font=200, command=self.start_menu)
        # leaderboard button
        self.leaderboardButton = tk.Button(self.master, text="Leaderboard", font=200, command=self.display_leaderboard)
        # Button to close leaderboard
        self.leaderboardcloseButton = tk.Button(self.master, text="Leaderboard", font=200, command=self.hide_leaderboard)
        # leaderboard button for in game
        self.leaderboardcloseButton2 = tk.Button(self.master, text="Leaderboard", font=200,command=self.start_menu)
    def start_menu(self):
        """Display the start menu and hide game elements."""
        self.hide_game_elements()
        self.hide_leaderboard()
        self.menuLabel.pack()
        self.playButton.place(x=200, y=650)
        self.leaderboardButton.place(x=200, y=400)
        self.backButton.place_forget()
    def start_game_from_menu(self):
        """Start the game from the menu, resetting all variables and displaying game elements."""
        self.hide_menu_elements()
        self.hide_leaderboard()
        self.show_game_elements()
        self.reset_game()
        self.e.focus_set()  # Ensure the entry widget is focused
        self.backButton.place(x=200, y=650)
        self.playButton.place_forget()

    def reset_game(self):
        """Reset the game variables and update the GUI elements accordingly."""
        self.score = 0
        self.timeleft = 60
        self.questions_left = 30
        self.return_count = 0
        self.scoreLabel.config(text="Score: 0")
        self.questionsLabel.config(text="Questions Left: 30/30")
        self.timeLabel.config(text=f"Time left: {self.timeleft}")
        self.label.config(text="", fg="black")

    def hide_game_elements(self):
        """Hide all game-related GUI elements."""
        self.instructions.pack_forget()
        self.scoreLabel.pack_forget()
        self.questionsLabel.pack_forget()
        self.timeLabel.pack_forget()
        self.label.pack_forget()
        self.e.pack_forget()
        self.startButton.pack_forget()
        self.backButton.pack_forget()

    def hide_menu_elements(self):
        """Hide all menu-related GUI elements."""
        self.menuLabel.pack_forget()
        self.playButton.place_forget()

    def show_game_elements(self):
        """Show all game-related GUI elements."""
        self.instructions.pack()
        self.scoreLabel.pack()
        self.questionsLabel.pack()
        self.timeLabel.pack()
        self.label.pack()
        self.e.pack()
        self.startButton.pack()
        self.backButton.pack()

    def hide_leaderboard(self):
        """Hide all leaderboard-related GUI elements."""
        if hasattr(self, 'leaderboard_label'):
            self.leaderboard_label.pack_forget()
        if hasattr(self, 'score_labels'):
            for label in self.score_labels:
                label.pack_forget()
        self.leaderboardcloseButton.place_forget()

    def write_score_to_file(self, score):
        """Write the final score to a file called 'leaderboard.txt'."""
        filename = 'leaderboard.txt'
        with open(filename, 'a') as f:
            f.write(f"{score}\n")

    def display_leaderboard(self):
        """Display the leaderboard with the top scores."""
        self.write_score_to_file(self.score)
        self.hide_game_elements()
        filename = 'leaderboard.txt'
        with open(filename, 'r') as f:
            scores = sorted([int(line.strip()) for line in f if line.strip().isdigit()], reverse=True)
        self.leaderboard_label = tk.Label(self.master, text="Leaderboard:", font=('Helvetica', 12))
        self.leaderboard_label.pack()
        self.score_labels = []
        for i, score in enumerate(scores[:10]):
            score_label = tk.Label(self.master, text=f"{i + 1}#  {score}", font=('Helvetica', 12))
            score_label.pack()
            self.score_labels.append(score_label)
        self.leaderboardcloseButton2.place(x=200,y=400)

    def start_game(self, event=None):
        """Handle the start of the game or the next question after pressing Enter."""
        self.return_count += 1
        self.questions_left -= 1
        self.questionsLabel.config(text=f"Questions Left: {self.questions_left}/30")

        if self.questions_left == 0:
            self.display_leaderboard()
        elif self.return_count == 1:
            self.countdown()
            self.next_color()
        else:
            self.next_color()

    def next_color(self):
        """Display the next color word and update the score if the previous input was correct."""
        if self.timeleft > 0:
            if self.e.get().lower() == self.colors[1].lower():
                self.score += 1
            self.e.delete(0, tk.END)
            random.shuffle(self.colors)
            self.label.config(fg=self.colors[1], text=self.colors[0])
            self.scoreLabel.config(text=f"Score: {self.score}")
            self.e.focus_set()  # Ensure the entry widget is focused

    def countdown(self):
        """Handle the countdown timer."""
        if self.timeleft > 0:
            self.timeleft -= 1
            self.timeLabel.config(text=f"Time left: {self.timeleft}")
            self.master.after(1000, self.countdown)


if __name__ == "__main__":
    # Initialize the main Tkinter window
    hydra = tk.Tk()
    hydra.title("Stroop Test")
    hydra.geometry("1820x1080")
    # Create an instance of the StroopTestGame
    game = StroopTestGame(hydra)
    # Bind the Return key to the start_game method
    hydra.bind('<Return>', game.start_game)
    # Change the Tkinter Icon
    # Icon
    photo = tk.PhotoImage(file='test.png')
    hydra.wm_iconphoto(False, photo)
    # Start the Tkinter main loop
    hydra.mainloop()
