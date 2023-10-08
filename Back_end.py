import os
import shutil

# Function to organize files in a directory
file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ai', '.psd', '.svg', '.webp', '.ico', '.ps'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xlsx', '.key', '.odp', '.pps', '.pptx', '.ods', '.xls', 'xlsm', '.odt', '.rtf', '.tex', '.wpd'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.3g2', '.3gp', '.flv', '.h264', '.m4v', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.webm', '.wmv'],
        'Music': ['.mp3', '.wav', '.flac', '.aif', '.cda', '.mid', '.midi', '.mpa', '.ogg', '.wma', '.wpl'],
        'Archives': ['.zip', '.rar', '.7z', '.arj', '.deb', '.pkg', '.rpm', '.z'],
        'Disc&Media': ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
        'Database': ['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'],
        'Webpages': ['.htm', '.html', '.xhtml', '.cer', '.part', '.jsp', '.asp'],
        'System Files': ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.ini', '.msi', '.sys', '.tmp'],
        'Executables': ['.apk', '.bat', '.bin', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.wsf'],
        'Developer': ['.c', '.cgi', '.pl', '.cpp', '.py', '.java', '.sh', '.swift', '.vb', '.php', '.h', '.class', '.cs'],
        'Others': [],  # For unrecognized file types
    }


def organize_files(source_folder):
    
    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1].lower()

            # Organize the file based on its type or move to 'Others'
            moved = False
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = os.path.join(source_folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(
                        target_folder, filename))
                    moved = True
                    break

            if not moved:
                # Create the target folder path for unrecognized files ('Others')
                target_folder = os.path.join(source_folder, 'Others')
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))


if __name__ == "__main__":
    source_directory = input(
        "Enter the path to the directory you want to organize: ")
    organize_files(source_directory)
    print("Files organized successfully!")

# Function to count the number of files in each category
def count_file_types(source_folder):
    counts = {}

    for folder_name, extensions in file_types.items():
        count = 0
        for filename in os.listdir(source_folder):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in extensions:
                count += 1
        counts[folder_name] = count

    return counts
