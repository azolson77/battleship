# This application was made to implement a simple one player game of battleship
# Written by Alex Olson
import random
from flask import *

# Boolean checking for victory
win = False
# Counter for number of turns
turn = 0
# Max number of turns
count = 10
# Initialize 2d board
board = [[]]
# Initialize coordinates for ship
coords = (-1, -1)
miss_message = ""


def make_board():
    global board
    board = [[0 for col in range(7)] for row in range(7)]
    return board


def show_board():
    for i in range(len(board)):
        print(board[i])
    print()


def attack(x, y):
    global win, turn, miss_message
    aim = (x, y)
    miss_message = "You shoot at " + str(aim) + ' and missed!'
    if coords == (x, y):
        win = True
        return win
    else:
        board[x][y] = -1


app = Flask(__name__)


@app.route('/')
def root():
    global board, win, coords
    board = make_board()
    battleship_x = random.randint(0, 6)
    battleship_y = random.randint(0, 6)
    coords = (battleship_x, battleship_y)
    location = "Battleship located at: " + str(coords)
    turns_left = "There are " + str(count - turn) + " turns left"
    return render_template('main.html', board=board, location=location, turns_left=turns_left)


@app.route('/calculate', methods=["POST"])
def calculate():
    global win, turn, count, miss_message
    turn += 1
    location = "Battleship located at: " + str(coords)
    turns_left = "Turns left: " + str(count - turn)
    # Pulls coordinates from POST request
    aim = request.form
    x = int(aim['X'])
    y = int(aim['Y'])

    win = attack(x, y)

    if win:
        return render_template('win.html', coords=coords)
    if turn == count:
        return render_template('lose.html', coords=coords)

    return render_template('main.html', board=board, location=location, turns_left=turns_left,
                           miss_message=miss_message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True,
            use_reloader=True)
