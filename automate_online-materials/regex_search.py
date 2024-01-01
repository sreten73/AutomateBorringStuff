#! python3
# regex_search - program that opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression.
# The results are printed to the screen.

import os
import re

# keep asking the user to enter a valid path until a valid path is entered
while True:
    # get the folder path from the user
    folder_path = input('Enter the folder path: ')
    # check if folder path exist
    if os.path.exists(folder_path):
        break
    else:
        print('Invalid path. Please enter a valid path.')

# get the regular expression from the user
regex_pattern = input('Enter the regular expression to search for: ')
# compile the regular expression
regex = re.compile(regex_pattern)

# iterate over all .txt files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        # open the file
        file_path = os.path.join(folder_path,filename)
        with open(file_path) as file:
            # search for lines that match the regular expression
            for line in file:
                if regex.search(line):
                    # print the matching line and the filename
                    print(f'{filename}: {line}')
