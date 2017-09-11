import random

def guess_number():
    number = random.randint(0, 2)
    counter = 0

    while counter < 5:
        guess = int(input('Guess a number between 0 and 20: '))
        if (guess == number):
            print('You guessed the right number!')
            break
        else:
            counter += 1
            continue

        print('Your number of turns ran out, the number was ')
        print(number)


guess_number()
