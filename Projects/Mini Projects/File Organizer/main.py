# Importing required modules
import os
import shutil

# Getting the input path from the user
path = input('Enter Path: ')

# Listing all files in the input path
files = os.listdir(path)

# Iterating through each file in the input path
for file in files:
    # Splitting the file name and extension
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Removing the leading dot from the extension

    # Checking if a directory with the same extension exists in the input path
    if os.path.exists(path+'/'+extension):
        # Moving the file to the directory with the corresponding extension
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        # If the directory with the extension doesn't exist, creating it
        os.makedirs(path+'/'+extension)
        # Moving the file to the newly created directory with the corresponding extension
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)