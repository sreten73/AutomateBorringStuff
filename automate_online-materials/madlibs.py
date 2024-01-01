import re

# Read the text file
with open('input.txt') as file:
    text = file.read()

# Define the regular expressions to find the placeholders
regex_adjective = re.compile(r'ADJECTIVE')
regex_noun = re.compile(r'NOUN')
regex_adverb = re.compile(r'ADVERB')
regex_verb = re.compile(r'VERB')

# Replace the placeholders with user input
text = regex_adjective.sub(input('Enter an adjective: '), text)
text = regex_noun.sub(input('Enter a noun: '), text)
text = regex_adverb.sub(input('Enter an adverb: '), text)
text = regex_verb.sub(input('Enter a verb: '), text)

# Print the modified text
print(text)

# Write the modified text to a new file
with open('output.txt', 'w') as file:
    file.write(text)
