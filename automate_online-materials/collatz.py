def collatz(num1):
    if num1 % 2 == 0:
        #print('Number ' + str(num1) + ' is even')
        nnum1 = num1 // 2
    else:
        nnum1 = 3 * num1 + 1
        #print(f'Number is odd so result is {nnum1}')
    print(nnum1)
    return nnum1

try:
    # PLease type integer number
    print('Enter an integer')
    newNumber = int(input())
    while newNumber != 1:
        newNumber = collatz(newNumber)
except:
    print('Please enter a valid integer number')