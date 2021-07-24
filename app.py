# This application was made to implement a simple one player game of battleship
# Written by Alex Olson
import random
from flask import *

# Boolean checking for victory
win = False

# Counter for number of turns
turn = 0
count = 10
board = [[]]
coords = (-1, -1)


def make_board():
    global board
    board = [[0 for col in range(10)] for row in range(10)]
    return board


def show_board():
    for i in range(len(board)):
        print(board[i])
    print()


def attack():
    global win
    x = int(input('Select x coordinate (0-9): '))
    y = int(input('Select y coordinate (0-9): '))
    aim = (x, y)
    print("You shoot at " + str(aim))
    if coords == (x, y):
        print("You sunk the battleship!")
        win = True
        return win
    else:
        print("Miss!")
        board[x][y] = -1


def place_ship():
    global win, coords
    battleship_x = random.randint(0, 10)
    battleship_y = random.randint(0, 10)
    coords = (battleship_x, battleship_y)
    print("Battleship located at: " + str(coords))


# Main game loop
def main():
    global turn
    make_board()
    place_ship()
    while not win:
        show_board()
        print("Turns left: " + str((count - turn)))
        # Check if turns left
        if turn == count:
            print("Out of ammo, you lose!")
            quit()
        attack()
        turn += 1


app = Flask(__name__)


@app.route('/')
def root():
    # main()
    return render_template('main.html', board=board)


@app.route('/calculate', methods=["POST"])
def calculate():
    global win, coords
    win = attack()

    if win:
        return render_template('win.html', coords=coords)

    return render_template('main.html', grid=board)




if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
