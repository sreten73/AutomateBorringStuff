#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# Phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (optional-so we use ?)
    (\s|-|\.)?                      # separator (optional)
    (\d{3})                         # first 3 digits
    (\s|-|\.)                      # separator (not optional)
    (\d{4})                         # last 4 digits
    (\s*(x|ext\.|ext)\s*(\d{2,5}))? # extension (optional)
)''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username (+ at the end ,match one or more)
    @                               # @ symbol
    [a-zA-Z0-9._]+                   # domain name
    (\.[a-zA-Z]{2,4})               # dot - something
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
#text = '''This is my phone number 381-643.0836 x39, and this is my email sreten98@mail.ru. Try to extraxt it, 381-643-0836 x39
#sreten98@mail.ru'''
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    print(phoneNum)
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        print(phoneNum)
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
print(matches)
# Copy result to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')