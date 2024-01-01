# This is a example of Collatz sequence

def collatz(n1):
    # Examine if the number even (parni ili neparni) number
    if n1%2 == 0:
        n2 = n1 // 2
    else:
        n2 = 3*n1 + 1
    return n2

try:
    print('Enter number:')
    num1 = int(input())

    num2 = collatz(num1)
    print(num2)

    while num2 != 1:
        num2 = collatz(num2)
        print(num2)
except:
    print('Invalid argument, please enter integer number')