<<<<<<< HEAD
"""
==============================================================================
CodeAlpha Internship

Project-3 : Task Automation with Python Scripts
Task-1    : JPG File Organizer

Author            : Muhammad Ali Haider
Date              : July 30, 2026
IDE               : Visual Studio Code 1.131.0
Python Version    : Python 3.14.6

Description:
Automatically organizes all JPG image files from the Downloads folder into a
new folder named "JPG Files". The program creates the destination folder if it
does not exist, moves all JPG files into it, and displays the total number of
files moved after completion.

Modules Used:
- os
- shutil
==============================================================================
"""

# Import required modules
import os          # Used for folder and file operations
import shutil      # Used to move files between folders

# Source folder containing the files
source_folder = "Downloads"

# Destination folder where JPG files will be moved
destination_folder = os.path.join(source_folder, "JPG Files")

# Get a list of all files inside the source folder
check = os.listdir(source_folder)

# Counter to keep track of the number of JPG files moved
count = 0

# Create the destination folder if it does not already exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Traverse each file in the source folder
for images in check:

    # Create the complete path of the current file
    source_path = os.path.join(source_folder, images)

    # Check if the file has a .jpg extension (case-insensitive)
    if images.lower().endswith(".jpg"):

        # Increase the count of moved files
        count += 1

        # Move the JPG file to the destination folder
        shutil.move(source_path, destination_folder)

# Display the final result
if count >= 1:
    print(f"{count} JPG file(s) moved successfully.")
else:
=======
"""
==============================================================================
CodeAlpha Internship

Project-3 : Task Automation with Python Scripts
Task-1    : JPG File Organizer

Author            : Muhammad Ali Haider
Date              : July 30, 2026
IDE               : Visual Studio Code 1.131.0
Python Version    : Python 3.14.6

Description:
Automatically organizes all JPG image files from the Downloads folder into a
new folder named "JPG Files". The program creates the destination folder if it
does not exist, moves all JPG files into it, and displays the total number of
files moved after completion.

Modules Used:
- os
- shutil
==============================================================================
"""

# Import required modules
import os          # Used for folder and file operations
import shutil      # Used to move files between folders

# Source folder containing the files
source_folder = "Downloads"

# Destination folder where JPG files will be moved
destination_folder = os.path.join(source_folder, "JPG Files")

# Get a list of all files inside the source folder
check = os.listdir(source_folder)

# Counter to keep track of the number of JPG files moved
count = 0

# Create the destination folder if it does not already exist
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)

# Traverse each file in the source folder
for images in check:

    # Create the complete path of the current file
    source_path = os.path.join(source_folder, images)

    # Check if the file has a .jpg extension (case-insensitive)
    if images.lower().endswith(".jpg"):

        # Increase the count of moved files
        count += 1

        # Move the JPG file to the destination folder
        shutil.move(source_path, destination_folder)

# Display the final result
if count >= 1:
    print(f"{count} JPG file(s) moved successfully.")
else:
>>>>>>> aefc2f7c5a0c4a6c555f06b1b9115337647c29a6
    print("No JPG Files Found!")