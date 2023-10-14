import os
from file_types import get_file_types  # Import the get_file_types function

def count_file_types(user_directory):
    file_types_dict = get_file_types()  # Get file types

    counts = {}
    for folder_name, extensions in file_types_dict.items():
        count = 0
        for filename in os.listdir(user_directory):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in extensions:
                count += 1
        counts[folder_name] = count

    return counts



