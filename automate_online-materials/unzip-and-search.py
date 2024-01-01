import shutil
import re
import os


# 1. Unzip file
shutil.unpack_archive("C://Users//jokics//Documents//ZNANJE//PYTHON//Notebook-Jupyter-Udemy-Complete-Python-3-Bootcamp-master//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//unzip_me_for_instructions.zip",\
'C://Users//jokics//Documents//ZNANJE//PYTHON//Notebook-Jupyter-Udemy-Complete-Python-3-Bootcamp-master//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//','zip')
# 1.1 Unzip file in current working direcotry
shutil.unpack_archive("C://Users//jokics//Documents//ZNANJE//PYTHON//Notebook-Jupyter-Udemy-Complete-Python-3-Bootcamp-master//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//unzip_me_for_instructions.zip",\
'','zip')


# 2. Read the instructions file
with open('C://Users//jokics//Documents//ZNANJE//PYTHON//Notebook-Jupyter-Udemy-Complete-Python-3-Bootcamp-master//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//extracted_content//Instructions.txt',\
          'r') as file1:
    contents = file1.read()
    print(contents)
with open('extracted_content//Instructions.txt',\
          'r') as file1:
    contents = file1.read()
    print(contents)

# 3. Regular Expression to Find the Link
pattern = r'\d{3}-\d{3}-\d{4}'
test_string = 'here is a random number 1231231234 , here is phone number formatted 123-123-1234'
print(re.findall(pattern, test_string))

# 4. Create a function for regex
def search(file,pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

# 5. OS Walk through the Files to Get the Link
results = []
for folder, sub_folders, files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        full_path = folder + '\\' + f
        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())