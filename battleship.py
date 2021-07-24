# This application was made to implement a simple one player game of battleship
# Written by Alex Olson
import random

# Boolean checking for victory
win = False

# Counter for number of turns
turn = 0
count = 10


def make_board():
    board = [[0 for col in range(10)] for row in range(10)]
    return board


def show_board(board):
    for i in range(len(board)):
        print(board[i])
    print()


def attack():
    x = int(input('Select x coordinate: '))
    y = int(input('Select y coordinate: '))
    aim = (x, y)
    print("You shoot at " + str(aim))
    if coords == (x, y):
        print("You sunk the battleship!")
        win = True
        quit()
    else:
        print("Miss!")
        board[x][y] = -1
    


# Coordinates of battleship on the game board
battleship_x = random.randint(0, 10)
battleship_y = random.randint(0, 10)
coords = (battleship_x, battleship_y)

print("Battleship located at: " + str(coords))

# Main game loop
board = make_board()
while not win:
    show_board(board)
    print("Turns left: " + str((count - turn)))
    # Check if turns left
    if turn == count:
        print("Out of ammo, you lose!")
        quit()
    attack()
    turn += 1
