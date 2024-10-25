import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="solar")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window geometry to full screen
root.geometry(f"{screen_width}x{screen_height}")

# Create buttons with ttkbootstrap styles
b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

# Run the application
root.mainloop()