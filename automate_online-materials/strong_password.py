import re

# check if password has lowercase, uppercase and digit
def check_password():

    while True:
        new_pass = input ( 'Please, set your new password: ' )

        if len(new_pass) < 8:
            print ( 'Please, your password is less than 8 characters. Try again.' )
            continue

        if lowcase.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a lowercase character' )
            print ( 'Please, try again to enter your password to use at least one lowercase' )
            continue

        if upcase.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a uperrcase character' )
            print ( 'Please, try again to enter your password to use at least one uppercase' )
            continue

        if digit.search(new_pass) == None:
            print ( 'The entered password doesn\'t have a digit character' )
            print ( 'Please, try again to enter your password to use at least one digit' )
            continue
        else:
            print ( 'New Password is valid and saved' )
            break
    return new_pass

lowcase = re.compile(r'[a-z]')
upcase = re.compile(r'[A-Z]')
digit = re.compile(r'(\d)')

new_pass_1 = check_password()

print(f'First four characters of your password are: {new_pass_1[0:4]}')