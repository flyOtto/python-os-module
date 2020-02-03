import os

# printing out the current directory
print(os.getcwd()) 

# changing directory with the path inserted
os.chdir('')

# printing out the list of the current directory
print(os.listdir())

# make a new directory in the directory
os.mkdir('RandomDirName')

# make new directory and sub-directory
os.makedirs('RandomDirName/RandomSubDirName')

# Removing directory and multilevel of directories
os.rmdir('RandomDirName')
os.removedirs('RandomDirName/RandomSubDirName')

# renaming file
os.rename('RandomDirName', 'randomDIRName')

# reading the information
print(os.stat('randomDIRName'))

