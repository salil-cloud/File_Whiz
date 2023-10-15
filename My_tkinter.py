from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
import os
from file_operations import count_file_types
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
upper_frame = tb.Labelframe(root, bootstyle="light", text="File_Whiz: Classify, Simplify, and Amplify Your File Management!", borderwidth=5, relief="raised")
upper_frame.pack(pady=20, padx=10, fill="x")

# Add menu button
my_menu = tb.Menubutton(upper_frame, bootstyle="info-outline", text="Explore")
my_menu.pack(pady=10, padx=10, side=LEFT)

# Configuring Inside menu
inside_menu = tb.Menu(my_menu)  

# Add content (a label) inside the frame
my_title = tb.Label(upper_frame, text="File_Whiz Application", font=("Pacifico", 22, "bold", "italic"), bootstyle="info")
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
                    Messagebox.show_warning(error_message, title="Directory Error")
                else:
                    # Call the count_file_types function to get category counts
                    counts = count_file_types(user_directory)

                    # Update the category labels in frame1
                    for category, count_label in zip(category_labels.keys(), category_labels.values()):
                        count = counts.get(category, 0)  # Get the count for the category
                        count_label.config(text=f"*   {count} Files Found | Type: {category} ")

                return user_directory

            # Create a frame for the user input
            input_frame = tb.Labelframe(new_tab,text='Step 1', bootstyle="info", borderwidth=5, relief="raised")
            input_frame.pack(side=TOP, fill=X, padx=40, pady=10)

            # Label and entry for directory input
            directory_label = tb.Label(input_frame, text="__Enter File Path__:", font=('Montserrat', 12, 'bold', 'underline'), bootstyle="inverse-primary", relief="groove")
            directory_label.pack(side=LEFT, padx=10, pady=5)
            
            # Browse button to select a directory
            browse_button = tb.Button(input_frame, text="Browse", command=browse_directory, bootstyle="info-outline")
            browse_button.pack(side=LEFT, padx=20, pady=5)

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
                label = tb.Label(frame1, text=f"*   0 : Files       | Type : {category} ", font=('Arial', 16, 'bold'), bootstyle="inverse-light", relief=RAISED)
                label.pack(padx=15, pady=15, anchor="w", fill=X)
                category_labels[category] = label  # Store the Label objects in the dictionary


            label2 = tb.Label(frame2, text='____Organize files by folder____', font=('Arial', 16, 'bold', 'underline'), bootstyle='inverse-primary', relief=RAISED)
            label2.pack(pady=20, padx=10)

            def creating_button() :
                button_label.config(text="Congratulations!! Your files are organized...")
            # Load the image for the button
            org_button = PhotoImage(file='File_Whiz/Images/Resized_loginbutton.png')

            # Create a label widget and set the image
            img_label = tb.Label(frame2, image=org_button, style='inverse-light')
            img_label.image = org_button  # Keep a reference to the image
            # img_label.pack(pady=20)

            # Create a custom style for the button
            button_style = 'my_custom.TButton'  # Define a custom style name

            # Configure the style to set the background color
            root.style.configure(button_style, background="#ffbf00", activebackground="#54B4D3", borderwidth=5, padding=(0, 0))

            # Create the button with the custom style
            img_button = tb.Button(frame2, image=org_button, command=creating_button, style=button_style)
            img_button.pack(pady=10)

            #creating label to show text after pressing the button
            button_label = tb.Label(frame2, text='', bootstyle='inverse-light')
            button_label.pack(pady=10)


            
# Function to open tabs when menu items are clicked
def open_home_tab():
    create_and_open_tab("Home")
    
def open_about_tab():
    create_and_open_tab("About")
    # Switch to the "About" tab
    notebook.select(section_tabs["About"])

def open_ref_materials_tab():
    create_and_open_tab("Reference Materials")
    # Switch to the "About" tab
    notebook.select(section_tabs["Reference Materials"])

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
inside_menu.add_command(label="Reference Materials", command=open_ref_materials_tab)
inside_menu.add_command(label="Contact Info", command=open_contact_info_tab)

# Associate the menu with menu button
my_menu['menu'] = inside_menu

# Open the "Home" tab initially
open_home_tab()

root.mainloop()
