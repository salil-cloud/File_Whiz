import os
from file_types import get_file_types  # Import the get_file_types function

def count_file_types(user_directory):
    try:
        file_types_dict = get_file_types()  # Get file types

        counts = {}
        for folder_name, extensions in file_types_dict.items():
            count = 0
            for filename in os.listdir(user_directory):
                file_extension = os.path.splitext(filename)[1].lower()
                if file_extension in extensions:
                    count += 1
            counts[folder_name] = count

        # Count "Others" by checking for unrecognized file extensions
        others_count = 0
        for filename in os.listdir(user_directory):
            file_extension = os.path.splitext(filename)[1].lower()
            found = False
            for extensions in file_types_dict.values():
                if file_extension in extensions:
                    found = True
                    break
            if not found:
                others_count += 1

        counts["Others"] = others_count

        return counts
    except Exception as e:
        # Handle the exception here
        print(f"An error occurred while counting file types: {e}")
        return None  # You can return None or an empty dictionary as needed
