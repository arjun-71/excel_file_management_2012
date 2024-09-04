import os

def count_files_in_folder(folder_path):
    try:
        # List all items in the directory
        items = os.listdir(folder_path)
        
        # Count only files (excluding directories)
        file_count = sum(1 for item in items if os.path.isfile(os.path.join(folder_path, item)))
        
        return file_count
    except FileNotFoundError:
        print(f"The folder at {folder_path} does not exist.")
        return 0
    except PermissionError:
        print(f"Permission denied to access the folder at {folder_path}.")
        return 0