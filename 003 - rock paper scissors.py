import random

# with conditions of the game inside the game in one function
def game():
    options = ['r', 'p', 's']
    computer = random.choice(options)
    player = input('Pick your weapon! Rock (R), Paper (P), or Scissors (S)?\n').lower()
    if computer != player:
        if player == 'p' and computer == 'r':
            print('You win! Paper beats Rock.')
        elif player == 's' and computer == 'p':
            print('You win! Scissors beat Paper.')
        elif player == 'r' and computer == 's':
            print('You win! Rock beats Scissors.')
        else:
            print('You lose!')
    else:
        print('It is a tie!')



# conditions of the game outside the game function 

# condition could be on 1 row ->>> if this OR this OR this - but then it won't have descriptive output message
def conditions(player1, player2):
        if player1 == 'p' and player2 == 'r':
            print('You win! Paper beats Rock.')
        elif player1 == 's' and player2 == 'p':
            print('You win! Scissors beat Paper.')
        elif player1 == 'r' and player2 == 's':
            print('You win! Rock beats Scissors.')
        else:
            print('You lose!')

def game2():
        options = ['r', 'p', 's']
        computer = random.choice(options)
        player = input('Pick your weapon! Rock (R), Paper (P), or Scissors (S)?\n').lower()

        if computer != player:
            conditions(player, computer)
        else:
            print('It is a tie!')

print(game2())