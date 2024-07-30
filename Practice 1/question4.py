import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)
        
        # Print the contents
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory you want to list
directory_path = '../../DSA C++'

# Call the function to list the contents of the directory
list_directory_contents(directory_path)
