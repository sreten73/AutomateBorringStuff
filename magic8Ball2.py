import random

messages = [ 'It is certain',
             'It is decidedly so',
             'Yes definetely',
             'Reply hazy try again',
             'Ask again later',
             'Concentrate and ask again',
             'My reply is no',
             'Outlook is not so good',
             'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

print('Four score and seven ' + \
'years ago...')