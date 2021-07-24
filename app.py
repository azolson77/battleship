# This application was made to implement a simple one player game of battleship
# Written by Alex Olson

from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():

    import random

    # Width and Height of the board
    WIDTH, HEIGHT = 10, 10

    # Variable containing the game board
    board = [[0 for col in range(WIDTH)] for row in range(HEIGHT)]

    # Coordinates of battleship on the game board
    battleship_x = random.randint(0, 10)
    battleship_y = random.randint(0, 10)
    coords = (battleship_x, battleship_y)

    # Boolean checking for victory
    win = False

    # Counter for number of turns
    turn = 0
    count = 10

    print("Battleship located at: " + str(coords))

    # Main game loop
    while not win:

        for i in range(len(board)):
            print(board[i])

        print("Turns left: " + str((count - turn)))

        # Check if turns left
        if turn == count:
            print("Out of ammo, you lose!")
            quit()

        # Get player input for x and y coords
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
            turn += 1
            print(board)



if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
