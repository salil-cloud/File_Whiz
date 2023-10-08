from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='vapor')
default_width = 1080
default_height = 800

# Set the default size
root.geometry(f"{default_width}x{default_height}")

# Set the minimum size to the default size
root.minsize(default_width, default_height)

# Set the maximum size to the default size
root.maxsize(default_width, default_height)

# Create the upper frame with a specified size
upper_frame = tb.Labelframe(root, bootstyle="light", text="File Organizer", borderwidth=5, relief="raised")
upper_frame.pack(pady=20, padx=10, fill="x")

# Add menu button
my_menu = tb.Menubutton(upper_frame, bootstyle="info-outline", text="Select Theme")
my_menu.pack(pady=10, padx=10, side=LEFT)

# Configuring Inside menu
inside_menu = tb.Menu(my_menu)  

# Add content (a label) inside the frame
my_title = tb.Label(upper_frame, text="File_Whiz Application", font=("Pacifico", 25, "bold", "italic"), bootstyle="info")
my_title.pack(pady=5, padx=160, side=LEFT)

# Load the image
image = PhotoImage(file='File_Whiz/Images/images1.png')

# Create a Label to display the image
image_label = Label(upper_frame, image=image)
image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected
image_label.pack(padx=5, side=RIGHT)

root.iconbitmap('File_Whiz/Images/Icon.ico')
root.title("FileWhiz Application")

root.mainloop()
