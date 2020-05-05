"""
    Name: Muhmammad Salman
    Milestone project2 (Tic Tac Toe upgrade)
"""
import random

from IPython.display import clear_output


# Function to display the board

def display_board(board):
    clear_output()

    print("-----------------------------")
    print('|1|  ' + board['1'] + '   |2|  ' + board['2'] + '   |3|  ' + board['3'] + '    |')
    print('---------+----------+--------')
    print('|4|  ' + board['4'] + '   |5|  ' + board['5'] + '   |6|  ' + board['6'] + '    |')
    print('---------+----------+--------')
    print('|7|  ' + board['7'] + '   |8|  ' + board['8'] + '   |9|  ' + board['9'] + '    |')
    print("-----------------------------")


# Ask Player 1 for there marker
def selectMarker():
    player1 = input("Please pick a marker 'X' or 'O' ")

    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print("Player 1 selected '", player1.upper(), "'. Player 2 will be '", player2, "'.")
            return player1.upper(), player2
            break

        elif player1.upper() == 'O':
            player2 = 'X'
            print("Player 1 selected '", player1.upper(), "'. Player 2 will be '", player2, "'.")
            return player1.upper(), player2
            break

        else:
            player1 = input("Please pick a marker 'X' or 'O' ")


def game(player1, player2):

    turn = choose_first()
    print(turn," turn first")
    if turn == 'Player 1':
        count = 0
    else:
        count = 1
    for i in range(11):
        display_board(new)

        # Player1 turn
        if (count % 2) == 0:

            print("Player1(" + player1 + ")")
            y = select_position()
            if y:
                new[y] = player1
                count += 1
                display_board(new)

        # Player2 turn
        else:
            print("Player2(" + player2 + ")")
            y = select_position()
            if y:
                new[y] = player2
                count += 1
                display_board(new)

        # Board check for winner
        if count > 5:
            result = win_check(player1, player2)
            if result:
                break

        # Out of move
        if count == 10:
            if end_game(new):
                print("\nGame Over.\n")
                print("It's a Tie!!")
                break

# select turn
def choose_first():
    if random.randrange(0,1) == 0:
        return 'Player 2'

    else:
        return 'Player 1'


# Check space
def space_check(board, x):
    if board[x] == ' ':
        return True
    else:
        return False

#Select position
def select_position ():
    move = input("Enter your place number: ")

    if space_check(new, move):
        return move
    else:
        print("That place is already taken try again")
        return False

# Win  check
def win_check(player1, player2):
    if new['7'] == new['8'] == new['9'] == 'X':  # across the top
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['4'] == new['5'] == new['6'] == 'X':  # across the middle
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['1'] == new['2'] == new['3'] == 'X':  # across the bottom
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['1'] == new['4'] == new['7'] == 'X':  # down the left side
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['2'] == new['5'] == new['8'] == 'X':  # down the middle
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['3'] == new['6'] == new['9'] == 'X':  # down the right side
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['7'] == new['5'] == new['3'] == 'X':  # diagonal
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    elif new['1'] == new['5'] == new['9'] == 'X':  # diagonal
        display_board(new)
        print("\nGame Over.\n")
        print("  player1(" + player1 + ") won. ")
        return True
    if new['7'] == new['8'] == new['9'] == 'O':  # across the top
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['4'] == new['5'] == new['6'] == 'O':  # across the middle
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['1'] == new['2'] == new['3'] == 'O':  # across the bottom
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['1'] == new['4'] == new['7'] == 'O':  # down the left side
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['2'] == new['5'] == new['8'] == 'O':  # down the middle
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['3'] == new['6'] == new['9'] == 'O':  # down the right side
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['7'] == new['5'] == new['3'] == 'O':  # diagonal
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True
    elif new['1'] == new['5'] == new['9'] == 'O':  # diagonal
        display_board(new)
        print("\nGame Over.\n")
        print("  player2(" + player2 + ") won. ")
        return True

#End of game
def end_game(board):
    for x in board:
        if board[x] == ' ':
            return False
        else:
            return True

#Play again?
def play_again():
        again = input("Enter Y to restart the game or enter N or anything else to quit ")
        if again.upper() == 'Y':
            return True
        else:
            return False

#main body
players = selectMarker()
new = {'1': ' ', '2': ' ', '3': ' ',
       '4': ' ', '5': ' ', '6': ' ',
       '7': ' ', '8': ' ', '9': ' '}

game(players[0], players[1])
while(play_again()):
    players = selectMarker()
    new = {'1': ' ', '2': ' ', '3': ' ',
           '4': ' ', '5': ' ', '6': ' ',
           '7': ' ', '8': ' ', '9': ' '}

    game(players[0], players[1])
