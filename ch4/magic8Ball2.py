import random, sys

messages = [
  'It is certain',
  'It is decidedly so',
  'Yes definitely',
  'Reply hazy try again',
  'Ask again later',
  'Concentrate and ask again',
  'My reply is no',
  'Outlook not so good',
  'Very doubtful'    
]

while True:
    print('Are you ready to for the answer? Enter Yes to proceed or No to quit')
    answer = input()
    
    if answer.casefold() == 'yes':
        print(messages[random.randint(0, len(messages) - 1)])
    elif answer.casefold() == 'no':
        print('Goodbye.')
        sys.exit()
    else:
        print('You must make a choice!')