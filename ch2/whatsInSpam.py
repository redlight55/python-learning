
spam = 0

while True:
    while True:
        print('Enter a number: ')
        
        try:
            spam = int(input())
        except ValueError:
            print('Not a number! Enter a number please!')
            break

        if spam == 1 or spam == 2:
            break
        else:
            print('Greetings!')
            break
    
    if spam == 1:
        print('Hello!')
    if spam == 2:
        print('Howdy!')