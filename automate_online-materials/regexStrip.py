#regexStrip.py - Regex Version of strip()

import re

def regex_strip(s, char=None):
    """
    Write a function that takes a string and does the same thing as the strip()
    string method. If no other arguments are passed other than the string to
    strip, then whitespace characters will be removed from the beginning and
    end of the string. Otherwise, the characters specified in the second argu-
    ment to the function will be removed from the string.
    """

    if not char:
        strip_left = re.compile(r'^\s*') #string starting with whitespace
        strip_right = re.compile(r'\s*$') #string ending with whitespace

        s = re.sub(strip_left, "", s) #replacing strip_left with "" in string s
        s = re.sub(strip_right, "", s) #replacing strip_right with "" in string s

    else:
        if char == '*':
            char1 = "r\'\\" + char + "\'"
            print(char1)
            strip_char = re.compile (char1)
            s = strip_char.sub ( "", s )
        else:
            strip_char = re.compile(char)
            s = strip_char.sub("", s)
    return s

if __name__ == '__main__':
    string_to_be_stripped = input("Enter string to be stripped: ")
    char_to_be_removed = input("Enter character to be removed, if none press enter: ")
    print(regex_strip(string_to_be_stripped, char_to_be_removed))