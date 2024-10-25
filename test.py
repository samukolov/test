import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")  # Width x Height

# Button click event
def on_button_click():
    messagebox.showinfo("Information", "Button was clicked!")

# Create and place a button
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=50)

# Run the application
root.mainloop()