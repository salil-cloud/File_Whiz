from tkinter import *
from ttkbootstrap.constants import *
from ttkbootstrap import Floodgauge
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
import os
from PIL import Image, ImageTk, ImageSequence
from pathlib import Path
from itertools import cycle
from file_operations import count_file_types
from Back_end import organize_files
from About_gui import get_about_text
from tkinter.filedialog import askdirectory

root = tb.Window(themename='vapor')
default_width = 1080
default_height = 880

# Set the default size
root.geometry(f"{default_width}x{default_height}")

# Set the minimum size to the default size
root.minsize(default_width, default_height)

# Set the maximum size to the default size
root.maxsize(default_width, default_height)

# Create the upper frame with a specified size
upper_frame = tb.Labelframe(
    root, bootstyle="light", text="File_Whiz: Classify, Simplify, and Amplify Your File Management!", borderwidth=5, relief="raised")
upper_frame.pack(pady=20, padx=10, fill="x")

# Add menu button
my_menu = tb.Menubutton(upper_frame, bootstyle="info-outline", text="Explore")
my_menu.pack(pady=10, padx=10, side=LEFT)

# Configuring Inside menu
inside_menu = tb.Menu(my_menu)

# Add content (a label) inside the frame
my_title = tb.Label(upper_frame, text="File_Whiz Application...", font=(
    "Pacifico", 22, "bold", "italic"), anchor="center", justify="center", bootstyle="info")
my_title.pack(pady=5, padx=26, side=LEFT)

# Load the image
image = PhotoImage(file='File_Whiz/Images/images1.png')

# Create a Label to display the image
image_label = Label(upper_frame, image=image,
                    anchor="center", justify="center")
# Keep a reference to the image to prevent it from being garbage collected
image_label.image = image
image_label.pack(padx=5, side=LEFT)

root.iconbitmap('File_Whiz/Images/Icon.ico')
root.title("FileWhiz Application")

# Create a Notebook (tabbed interface) for the sections
notebook = tb.Notebook(root)
notebook.pack(fill='both', expand=True)

# Dictionary to store the section tabs
section_tabs = {}

# Function to create and open a new tab for a section


def create_and_open_tab(section_name):
    if section_name not in section_tabs:
        new_tab = Frame(notebook)
        notebook.add(new_tab, text=section_name)
        section_tabs[section_name] = new_tab
        if section_name != "Home":
            close_frame = Frame(new_tab)
            close_frame.pack(side=TOP, anchor="ne")
            close_button = Button(
                close_frame, text="Close", command=lambda name=section_name: close_current_tab(name))
            close_button.pack()

        if section_name == "Home":
            # Function to open a directory selection dialog
            def browse_directory():
                selected_directory = askdirectory()
                if selected_directory:
                    directory_entry.delete(0, END)  # Clear the entry
                    directory_entry.insert(0, selected_directory)

            # Function to save the directory path
            user_directory = ""

            def save_directory():
                global user_directory
                user_directory = str(directory_entry.get())

                if not os.path.exists(user_directory):
                    # The specified directory does not exist
                    error_message = "The specified directory does not exist."
                    Messagebox.show_warning(
                        error_message, title="Directory Error")
                else:
                    # Call the count_file_types function to get category counts
                    counts = count_file_types(user_directory)

                    # Update the category labels in frame1
                    for category, count_label in zip(category_labels.keys(), category_labels.values()):
                        # Get the count for the category
                        count = counts.get(category, 0)
                        count_label.config(
                            text=f"*   {count} Files Found | Type: {category} ")

                return user_directory

            # Create a frame for the user input
            input_frame = tb.Labelframe(
                new_tab, text='Step 1', bootstyle="info", borderwidth=5, relief="raised")
            input_frame.pack(side=TOP, fill=X, padx=40, pady=10)

            # Label and entry for directory input
            directory_label = tb.Label(input_frame, text="__Enter File Path__:", font=(
                'Pacifico', 12, 'bold', 'underline'), bootstyle="inverse-primary", relief="groove")
            directory_label.pack(side=LEFT, padx=10, pady=5)

            # Browse button to select a directory
            browse_button = tb.Button(
                input_frame, text="Browse", command=browse_directory, bootstyle="info-outline")
            browse_button.pack(side=LEFT, padx=20, pady=5)

            # Create an Entry widget to input the directory path
            directory_entry = tb.Entry(
                input_frame, font=('Pacifico', 12), bootstyle="light")
            directory_entry.pack(
                side=LEFT, fill=X, expand=True, padx=10, pady=10)

            # Button to save directory
            save_button = tb.Button(
                input_frame, text="SUBMIT", command=save_directory, bootstyle="danger")
            save_button.pack(side=LEFT, padx=20, pady=5)

            # Create two frames in the "Home" tab
            frame1 = tb.Frame(new_tab, bootstyle="light", relief=SUNKEN)
            frame2 = tb.Frame(new_tab, bootstyle="light", relief=SUNKEN)

            #  Use the pack geometry manager to place the frames side by side
            frame1.pack(side=LEFT, fill=Y, expand=True, padx=10, pady=10)
            frame2.pack(side=RIGHT, fill=Y, expand=True, padx=10, pady=10)

            # Add content to the frames (you can customize this)
            label1 = tb.Label(frame1, text='File counts by folder', font=(
                "Pacifico", 16, 'bold'), anchor="center", justify="center", bootstyle="inverse-info", relief=RAISED)
            label1.pack(pady=10, padx=10, fill=X)

            # Create labels for the categories and display the number of files
            category_labels = {
                "Images": None,
                "Documents": None,
                "Videos": None,
                "Music": None,
                "Archives": None,
                "Disc&Media": None,
                "Others": None,
            }

            # Create and pack labels for each category
            for category, count_label in category_labels.items():
                label = tb.Label(frame1, text=f"*   0 : Files       | Type : {category} ", font=(
                    "Pacifico", 16, 'bold'), bootstyle="inverse-light", relief=RAISED)
                label.pack(padx=15, pady=15, anchor="w", fill=X)
                # Store the Label objects in the dictionary
                category_labels[category] = label

            label2 = tb.Label(frame2, text='     Step - 2 : Click to organize     ', font=('Pacifico',
                              16, 'bold'), anchor="center", justify="center", bootstyle='inverse-info', relief=RAISED)
            label2.pack(pady=10, padx=10, fill=X)

            # Define the variable with a default value
            congratulations_gif_path = Path(
                "File_Whiz/Images/Welcome_user.gif")

            def creating_button():
                # Get the user's selected directory
                user_directory = str(directory_entry.get())
                if user_directory:
                    # Start the Floodgauge
                    gauge.start()
                    # Organize Files
                    organize_files(user_directory)
                    # Stop the Floodgauge
                    gauge.stop()
                    Completion_message = "Wonderful job! Your files are now elegantly sorted and all set"
                    Messagebox.show_info(
                        Completion_message, title="Task Completed")
                else:
                    error_message = "Please select a directory first."
                    Messagebox.show_warning(
                        error_message, title="Directory Missing")
            # Load the image for the button
            org_button = PhotoImage(
                file='File_Whiz/Images/Resized_loginbutton.png')

            # Create a label widget and set the image
            img_label = tb.Label(frame2, image=org_button,
                                 style='inverse-light')
            img_label.image = org_button  # Keep a reference to the image
            # img_label.pack(pady=20)

            # Create a custom style for the button
            button_style = 'my_custom.TButton'  # Define a custom style name

            # Configure the style to set the background color
            root.style.configure(button_style, background="#44d7e8",
                                 activebackground="#54B4D3", borderwidth=0, padding=(0, 0), relief=SUNKEN)

            # Create the button with the custom style
            img_button = tb.Button(
                frame2, image=org_button, command=creating_button, style=button_style)
            img_button.pack(pady=5)

            # Create a Floodgauge widget
            completed = "Files Arranged"
            gauge = Floodgauge(frame2, bootstyle=PRIMARY, font=(
                'Pacifico', 14, 'bold'), mask='Memory Used {}%', maximum=100)
            gauge.pack(fill=X, expand=YES, padx=10, pady=(0, 5))

            # Adjust the path to your animated GIF file
            congratulations_gif_path = Path(
                "File_Whiz/Images/Welcome_user.gif")
            with Image.open(congratulations_gif_path) as im:
                # Create a sequence
                sequence = ImageSequence.Iterator(im)
                images = [ImageTk.PhotoImage(s) for s in sequence]
                congratulations_image_cycle = cycle(images)

                # Duration of each frame
                framerate = im.info["duration"]

            # Create a label to display the GIF
            congratulations_label = tb.Label(frame2, image=next(
                congratulations_image_cycle), borderwidth=5)
            congratulations_label.pack(fill="both", expand="yes")

            def next_frame():
                """Update the image for each frame"""
                congratulations_label.configure(
                    image=next(congratulations_image_cycle))
                congratulations_label.after(framerate, next_frame)

            congratulations_label.after(framerate, next_frame)

        if section_name == "About":
            About_tab = tb.Label(new_tab, text=get_about_text(), font=(
            "Pacifico", 12, "italic"), anchor="center", justify="center", bootstyle="default")
            About_tab.pack(pady=5, padx=26, side=TOP)

        if section_name == "How to Operate":
            About_tab = tb.Label(new_tab, text="Learn How to Operate..", font=(
            "Pacifico", 12, "bold"), anchor="center", justify="center", bootstyle="default")
            About_tab.pack(pady=5, padx=26, side=TOP)

            image = PhotoImage(file='File_Whiz/Images/How_to.png')
            # Create a Label to display the image
            image_label = Label(new_tab, image=image,
                        anchor="center", justify="center", borderwidth=0)
            # Keep a reference to the image to prevent it from being garbage collected
            image_label.image = image
            image_label.pack(padx=5)

        if section_name == "Contact Info":
            About_tab = tb.Label(new_tab, text="Dev/Author : Salil Debnath", font=(
            "Pacifico", 12), anchor="center", justify="center", bootstyle="default")
            About_tab.pack(pady=5, padx=26, side=TOP)
            image = PhotoImage(file='File_Whiz/Images/About_linkedin.png')
            # Create a Label to display the image
            image_label = Label(new_tab, image=image,
                        anchor="center", justify="center", borderwidth=0)
            # Keep a reference to the image to prevent it from being garbage collected
            image_label.image = image
            image_label.pack(padx=5)


# Function to open tabs when menu items are clicked
if __name__ == "__main__":
    def open_home_tab():
        create_and_open_tab("Home")
        root.mainloop()


def open_about_tab():
    create_and_open_tab("About")
    # Switch to the "About" tab
    notebook.select(section_tabs["About"])


def open_How_to_tab():
    create_and_open_tab("How to Operate")
    # Switch to the "About" tab
    notebook.select(section_tabs["How to Operate"])


def open_contact_info_tab():
    create_and_open_tab("Contact Info")
    # Switch to the "About" tab
    notebook.select(section_tabs["Contact Info"])

# Function to close a specific tab


def close_current_tab(section_name):
    tab_to_close = section_tabs.get(section_name)
    if tab_to_close:
        notebook.forget(tab_to_close)
        del section_tabs[section_name]


# Add menu items that open the respective tabs
inside_menu.add_command(label="Home", command=open_home_tab)
inside_menu.add_command(label="About", command=open_about_tab)
inside_menu.add_command(label="How to Operate",
                        command=open_How_to_tab)
inside_menu.add_command(label="Contact Info", command=open_contact_info_tab)

# Associate the menu with menu button
my_menu['menu'] = inside_menu

# Open the "Home" tab initially
open_home_tab()

root.mainloop()
