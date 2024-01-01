import re

text = input('Enter string to be stripped: ')
char = input('Enter character to be removed, if none press enter:')
vowelRegex = re.compile(r'[a-zA-Z0-9]')
t = vowelRegex.findall(char)
if t:
    char1 = char
    print(char1)
else:
    char1 = "\\" + char
    print(char1)
#char2 = re.compile(r'\*')


if not char:
    strip_left = re.compile(r'^\s*') #string starting with whitespace
    strip_right = re.compile(r'\s*$') #string ending with whitespace

    text = re.sub(strip_left, "", text) #replacing strip_left with "" in string s
    text = re.sub(strip_right, "", text) #replacing strip_right with "" in string s
    s2 = text

else:
    #for i in range(len(char1)):

        #char2 = re.compile('({})'.format(char1))
     #   char3 = re.compile('({})'.format(char1[i]))

        #s1 = char2.sub(r'', '****Output****')
      #  s2 = char3.sub(r'', text)
    br_first_letter = 0
    for i in range(len(text)):
        for j in range(len(char1)):
            if text[i] == char[j]:
                char3 = re.compile ( '({})'.format ( char1[j] ) )
                s2 = char3.sub ( r'', text )
            else:
                br_first_letter += 1
        if br_first_letter == len(char1):
            break


#print(s1)
print(s2)




