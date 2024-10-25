import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window to fit the screen
root.geometry(f"{screen_width}x{screen_height}")

# Button click event
def on_button_click():
    messagebox.showinfo("Information", "Button was clicked!")

# Create and place a button
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=50)

# Run the application
root.mainloop()
