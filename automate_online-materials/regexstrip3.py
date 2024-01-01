#regexStrip.py - Regex Version of strip()

import re

def stripRegex(s,toStrip=None):
    """
        Write a function that takes a string and does the same thing as the strip()
        string method. If no other arguments are passed other than the string to
        strip, then whitespace characters will be removed from the beginning and
        end of the string. Otherwise, the characters specified in the second argu-
        ment to the function will be removed from the string.
        """
    if toStrip is None:
        toStrip = '\s' #string starting or ending with whitespace
    return re.sub(r'^[{0}]+|[{0}]+$'.format(toStrip), '', s) #replacing toStrip with "" in string s

#Examples
x1 = ''
x2 = 'Spam'
x3 = 'pSam'
string1 = '      Hello world!!!   '
string2 = 'SpamSpamBaconSpamEggsSpamSpam'

print(stripRegex(string1)) # 'Hello world!!!'
print(stripRegex(string1, x1)) # '      Hello world!!!   '
print(stripRegex(string2, x2)) # 'BaconSpamEggs'
print(stripRegex(string2, x3)) # 'BaconSpamEggs'

if __name__ == '__main__':
    string_to_be_stripped = input("Enter string to be stripped: ")
    char_to_be_removed = input("Enter character to be removed, if none press enter: ")
    print(stripRegex(string_to_be_stripped, char_to_be_removed))