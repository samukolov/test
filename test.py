import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="solar")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window geometry to full screen
root.geometry(f"{screen_width}x{screen_height}")



# Sidebar Frame
sidebar = ttk.Frame(root, width=200, bootstyle="primary")
sidebar.pack(side=LEFT, fill=Y)

# Three buttons in the sidebar
b1 = ttk.Button(sidebar, text="Dashboard", bootstyle=SUCCESS)
b1.pack(fill=X, padx=10, pady=10)

b2 = ttk.Button(sidebar, text="Settings", bootstyle=INFO)
b2.pack(fill=X, padx=10, pady=10)

b3 = ttk.Button(sidebar, text="Help", bootstyle=DANGER)
b3.pack(fill=X, padx=10, pady=10)



# Main content area
main_content = ttk.Frame(root)
main_content.pack(side=LEFT, fill=BOTH, expand=True)

# Example content in the main area
label = ttk.Label(main_content, text="Main Content Area", font=("Helvetica", 24))
label.pack(pady=20)

# Run the application
root.mainloop()