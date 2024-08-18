def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
print('Enter a number')
numInput = input()

try:
    collatzValue = int(numInput)

    while collatzValue > 1:
        collatzValue = collatz(collatzValue)
        print(collatzValue)
        
except ValueError:
    print('You must enter an integer!')