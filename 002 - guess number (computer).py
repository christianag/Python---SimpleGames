import random


def guess_game():

    do_you_want_to_play_again = True

    while do_you_want_to_play_again:

        x = int(input('Give me a number as a lower base!\n'))
        y = int(input('Now give me a number as an upper base!\n'))
        if x != 0 and y != 0:
            feedback = ''
            while feedback != 'Y':
                computers_guess = random.randint(x, y)
                feedback = input(f'Is your number {computers_guess}? \nYes (Y), too low (L), or too high (H)? \n').upper()
                if feedback == 'L':
                    x = computers_guess + 1
                elif feedback == 'H':
                    y = computers_guess - 1

            print(f'I guessed it! Your number is {computers_guess}')

            go_again = input('\nWould you like to play again? (Y/N)\n').upper()
            if go_again == 'Y':
                do_you_want_to_play_again = True
            else:
                do_you_want_to_play_again = False

        else:
            print('You cannot pick 0 as either base!')


guess_game()

