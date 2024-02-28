import random

computer_number = random.randrange(1,10)

while True:
    print('Guess a number between 1 and 10:')
    user_number = int(input())

    if user_number == computer_number:
        print('Congrats, you win!')
        break
    else:
        print('Try again!')

    

