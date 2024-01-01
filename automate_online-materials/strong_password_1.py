import re

pasword = re.compile ( r'''(
 \d+ #have at lest one digit
 .* # anything
 [A-Z]+ # at least 1 capital
 .*
 [a-z]+ # at least one lower
 .* 
 )''', re.VERBOSE )

# test
pasword.search ( '1@#A!a' ).group ()


def is_strong_password():
    pas = input ( 'Enter a password:' )


    if len ( pas ) < 8:
        print ( 'Not strong pasword' )
        return False
    else:
        check = pasword.search(''.join(sorted(pas))).group()  # sorted is important to be sure that user can write symbols in any order he/she wants
    if (not check):
        print ( 'Not strong pasword' )
        return False
    else:
        print ( 'Strong password' )
        return True

print(is_strong_password())