import os

# Specify the directory path
directory_path = 'D:/python/API_Automation'

try:
    # Get the list of all files and directories
    items = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in items:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
