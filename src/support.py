import os

# Define the path where you want to create the folders
base_path = "Data"

# Create the base directory if it doesn't exist
if not os.path.exists(base_path):
    os.mkdir(base_path)

# Create folders from A to Z
for letter in "0123456789":
    folder_name = os.path.join(base_path, letter)
    
    # Check if the folder already exists before creating it
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

print("Folders from A to Z have been created.")