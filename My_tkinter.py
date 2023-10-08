from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='vapor')
default_width = 980
default_height = 700

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
my_menu = tb.Menubutton(upper_frame, bootstyle="info-outline", text="Explore")
my_menu.pack(pady=10, padx=10, side=LEFT)

# Configuring Inside menu
inside_menu = tb.Menu(my_menu)  

# Add content (a label) inside the frame
my_title = tb.Label(upper_frame, text="File_Whiz Application", font=("Pacifico", 35, "bold", "italic"), bootstyle="info")
my_title.pack(pady=5, padx=160, side=LEFT)

# Load the image
image = PhotoImage(file='File_Whiz/Images/images1.png')

# Create a Label to display the image
image_label = Label(upper_frame, image=image)
image_label.image = image  # Keep a reference to the image to prevent it from being garbage collected
image_label.pack(padx=5, side=RIGHT)

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
            close_button = Button(close_frame, text="Close", command=lambda name=section_name: close_current_tab(name))
            close_button.pack()

        if section_name == "Home":
            # Function to save user directory
            def save_directory():
                user_directory = directory_entry.get()
                return user_directory  ########################################### use this 
                # You can now use the 'user_directory' variable for further processing

            # Create a frame for the user input
            input_frame = tb.Frame(new_tab, bootstyle="dark", relief=SUNKEN)
            input_frame.pack(side=TOP, fill=X, padx=40, pady=10)

            # Label and entry for directory input
            directory_label = tb.Label(input_frame, text="__Enter File Path__:", font=('Arial', 12, 'bold', 'underline'), bootstyle="inverse-primary", relief="groove")
            directory_label.pack(side=LEFT, padx=10, pady=5)
            
            # Function to save the directory path
            user_directory = ""

            def save_directory():
                global user_directory
                user_directory = directory_entry.get()
                # You can now use the 'user_directory' variable for further processing

            # Create an Entry widget to input the directory path
            directory_entry = tb.Entry(input_frame, font=('Arial', 12), bootstyle="light")
            directory_entry.pack(side=LEFT, fill=X, expand=True, padx=10, pady=10)

            # Button to save directory
            save_button = tb.Button(input_frame, text="SUBMIT", command=save_directory, bootstyle="danger")
            save_button.pack(side=LEFT, padx=20, pady=5)

            
            # Create two frames in the "Home" tab
            frame1 = tb.Frame(new_tab, bootstyle="light", relief=SUNKEN)
            frame2 = tb.Frame(new_tab, bootstyle="light", relief=SUNKEN)

            #  Use the pack geometry manager to place the frames side by side
            frame1.pack(side=LEFT, fill=Y, expand=True, padx=10, pady=10)
            frame2.pack(side=RIGHT, fill=Y, expand=True, padx=10, pady=10)


            # Add content to the frames (you can customize this)
            label1 = tb.Label(frame1, text='______File counts by folder______', font=('Arial', 16, 'bold', 'underline'), bootstyle="inverse-primary", relief=RAISED)
            label1.pack(pady=20, padx=10)

            label2 = tb.Label(frame2, text='____Organize files by folder____', font=('Arial', 16, 'bold', 'underline'), bootstyle='inverse-primary', relief=RAISED)
            label2.pack(pady=20, padx=10)
            



# Function to open tabs when menu items are clicked
def open_home_tab():
    create_and_open_tab("Home")
    
def open_about_tab():
    create_and_open_tab("About")

def open_ref_materials_tab():
    create_and_open_tab("Reference Materials")

def open_contact_info_tab():
    create_and_open_tab("Contact Info")

# Function to close a specific tab
def close_current_tab(section_name):
    tab_to_close = section_tabs.get(section_name)
    if tab_to_close:
        notebook.forget(tab_to_close)
        del section_tabs[section_name]

# Add menu items that open the respective tabs
inside_menu.add_command(label="Home", command=open_home_tab)
inside_menu.add_command(label="About", command=open_about_tab)
inside_menu.add_command(label="Reference Materials", command=open_ref_materials_tab)
inside_menu.add_command(label="Contact Info", command=open_contact_info_tab)

# Associate the menu with menu button
my_menu['menu'] = inside_menu

# Open the "Home" tab initially
open_home_tab()

root.mainloop()
