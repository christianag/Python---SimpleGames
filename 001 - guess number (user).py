import random

def guess_game():

    do_you_want_to_play_again = True

    while do_you_want_to_play_again:

        x = int(input('Give me your lower base! \n'))
        y = int(input('Now give me your upper base! \n'))
        random_number = random.randint(x, y)
        guess = 0
        
        if x != y and x != 0 and y != 0:
            while guess != random_number:
                guess = int(input(f'I thought of a number between {x} and {y}. Guess what it is! \n'))
                if guess > random_number:
                    print('Your guess is too high!')
                elif guess < random_number:
                    print('Your guess it too low!')
                else: 
                    print(f'Yes! You guessed it! The number is {random_number}')
                    go_again = input('\nWould you like to play again? (Y/N) \n').upper()
                    if go_again == 'Y':
                        do_you_want_to_play_again = True
                    else:
                        do_you_want_to_play_again = False

        else: 
            print('The numbers cannot be the same or a zero!')


print(guess_game())