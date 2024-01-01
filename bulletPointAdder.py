#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()
print(text)

# Separate lines and add stars.
lines = text.split('\n')
print(lines[0])
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
print(lines[0])
text = '\n'.join(lines)
print(text)
pyperclip.copy(text)