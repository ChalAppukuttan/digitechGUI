import tkinter as tk

# Create main application window
root = tk.Tk()

# Set the title of the window
root.title("Tkinter Tutorial")

# Set the size of the window
root.geometry("400x300")

# Function to execute when button is clicked
def button_click():
    label.config(text="Button clicked!")

# Create a label widget
label = tk.Label(root, text="Tkinter Tutorial", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=2)  # Place label in the first row and spans across two columns

# Create buttons
button1 = tk.Button(root, text="Button 1", command=button_click)
button1.grid(row=1, column=0)  # Place button1 in the second row and first column

button2 = tk.Button(root, text="Button 2", command=button_click)
button2.grid(row=1, column=1)  # Place button2 in the second row and second column

button3 = tk.Button(root, text="Button 3", command=button_click)
button3.grid(row=2, column=0, columnspan=2, sticky="ew")  # Place button3 in the third row and spans across two columns, sticky="ew" expands button horizontally

# Run the application
root.mainloop()
