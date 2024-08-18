import random, sys

while True:
    def getAnswer(number):
        if number == 1:
            return 'It is certain'
        if number == 2:
            return 'It is decidedly so'
        if number == 3:
            return 'Yes'
        if number == 4:
            return 'Reply hazy try again'
        if number == 5:
            return 'Ask again later'
        if number == 6:
            return 'Concentrate and ask again'
        if number == 7:
            return 'My reply is no'
        if number == 8:
            return 'Outlook not so good'
        if number == 9:
            return 'Very doubtful'

    print('Are you ready to know your fate?')
    print('Type `yes` to roll or `no` to quit')
    playerInput = input()

    if playerInput.casefold() == 'yes':
        randomInt = random.randint(1, 9)
        fortune = getAnswer(randomInt)
        print(fortune)

        ## This also works if you want to skip the whole typing
        #print(getAnswer(random.randint(1, 9)))

    elif playerInput.casefold() == 'no':
        print('Very well. Your fate shall remain hidden.')
        sys.exit()
    else:
        print('You must make your choice!')