import tkinter as tk
import random



class StroopTestGame:
    def __init__(self, master):
        self.master = master
        self.colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
        self.score = 0
        self.timeleft = 60
        self.questions_left = 30
        self.return_count = 0

        self.setup_widgets()
        self.start_menu()

    def setup_widgets(self):
        self.instructions = tk.Label(self.master, text="Type in the color of the words, not the word text!",
                                     font=('Helvetica', 12))
        self.scoreLabel = tk.Label(self.master, text="Press enter to start", font=('Helvetica', 12))
        self.questionsLabel = tk.Label(self.master, text="Questions Left: 30/30", font=('Helvetica', 12))
        self.timeLabel = tk.Label(self.master, text=f"Time left: {self.timeleft}", font=('Helvetica', 12))
        self.label = tk.Label(self.master, font=('Helvetica', 60))
        self.e = tk.Entry(self.master)
        self.startButton = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.menuLabel = tk.Label(self.master, text="Welcome to the Stroop Test Game!", font=('Helvetica', 30))
        self.playButton = tk.Button(self.master, text="Play", command=self.start_game_from_menu)

    def start_menu(self):
        self.hide_game_elements()
        self.menuLabel.pack()
        self.playButton.pack()

    def start_game_from_menu(self):
        self.hide_menu_elements()
        self.show_game_elements()
        self.reset_game()
        self.e.focus_set()

    def reset_game(self):
        self.score = 0
        self.timeleft = 60
        self.questions_left = 30
        self.return_count = 0
        self.scoreLabel.config(text="Score: 0")
        self.questionsLabel.config(text="Questions Left: 30/30")
        self.timeLabel.config(text=f"Time left: {self.timeleft}")
        self.label.config(text="", fg="black")

    def hide_game_elements(self):
        self.instructions.pack_forget()
        self.scoreLabel.pack_forget()
        self.questionsLabel.pack_forget()
        self.timeLabel.pack_forget()
        self.label.pack_forget()
        self.e.pack_forget()
        self.startButton.pack_forget()

    def hide_menu_elements(self):
        self.menuLabel.pack_forget()
        self.playButton.pack_forget()

    def show_game_elements(self):
        self.instructions.pack()
        self.scoreLabel.pack()
        self.questionsLabel.pack()
        self.timeLabel.pack()
        self.label.pack()
        self.e.pack()
        self.startButton.pack()

    def write_score_to_file(self, score):
        filename = 'leaderboard.txt'
        with open(filename, 'a') as f:
            f.write(f"{score}\n")

    def display_leaderboard(self):
        self.write_score_to_file(self.score)
        self.hide_game_elements()
        filename = 'leaderboard.txt'
        with open(filename, 'r') as f:
            scores = sorted([int(line.strip()) for line in f if line.strip().isdigit()], reverse=True)

        leaderboard_label = tk.Label(self.master, text="Leaderboard:", font=('Helvetica', 12))
        leaderboard_label.pack()
        for i, score in enumerate(scores[:10]):
            score_label = tk.Label(self.master, text=f"{i + 1}#  {score}", font=('Helvetica', 12))
            score_label.pack()

    def start_game(self, event=None):
        self.return_count += 1
        self.questions_left -= 1
        self.questionsLabel.config(text=f"Questions Left: {self.questions_left}/30")

        if self.questions_left == 0:
            self.display_leaderboard()
        elif self.return_count == 1:
            self.countdown()
            self.next_color()

    def next_color(self):
        if self.timeleft > 0:
            if self.e.get().lower() == self.colors[1].lower():
                self.score += 1
            self.e.delete(0, tk.END)
            random.shuffle(self.colors)
            self.label.config(fg=self.colors[1], text=self.colors[0])
            self.scoreLabel.config(text=f"Score: {self.score}")

    def countdown(self):
        if self.timeleft > 0:
            self.timeleft -= 1
            self.timeLabel.config(text=f"Time left: {self.timeleft}")
            self.master.after(1000, self.countdown)


if __name__ == "__main__":
    hydra = tk.Tk()
    hydra.title("Stroop Test")
    hydra.geometry("1820x1080")
    game = StroopTestGame(hydra)
    hydra.bind('<Return>', game.start_game)
    hydra.mainloop()
