import os
import shutil
import My_tkinter
import file_types



def organize_files(user_directory):
    
    # Iterate through files in the source folder
    for filename in os.listdir(user_directory):
        file_path = os.path.join(user_directory, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()

            # Organize the file based on its type or move to 'Others'
            moved = False
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = os.path.join(user_directory, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(
                        target_folder, filename))
                    moved = True
                    break

            if not moved:
                # Create the target folder path for unrecognized files ('Others')
                target_folder = os.path.join(user_directory, 'Others')
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

# This function only for command line testung/usage
# if __name__ == "__main__":   # remove it and do this task through Tkinter application
#     source_directory = input(
#         "Enter the path to the directory you want to organize: ")
#     organize_files(source_directory)
#     print("Files organized successfully!")
