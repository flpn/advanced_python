import os
import shutil

# Current work directory
os.getcwd()   # as a string
os.getcwdb()  # as bytes


# Changing current directory
os.chdir('/home/flpn')


# List directories and files
os.listdir(os.getcwd())  # returns a list with the names of all directories and files from the path passed as argument


# Making a new directory
os.mkdir('new_directory')


# Renaming a directory
os.rename('new_directory', 'directory_renamed')


# Removing Directory or File
os.remove('test.txt')
os.rmdir('directory_renamed')      # removes an empty directory
shutil.rmtree('fully_directory')  # removes a non-empty directory
