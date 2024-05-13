import tkinter as tk

hydra = tk.Tk()
hydra.title = ("Tkinter")
hydra.geometry("400x300")

def button_click():
    label.config(text="Button clicked!")


label = tk.Label(hydra, text="Hello, Tkinter!")
label.pack()

button = tk.Button(hydra,text="click me", command=button_click)
button.pack()

hydra.mainloop()  # Tells the window to run

