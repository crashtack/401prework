"""
    A Simple Game of Battleship
"""

from random import randint

board = []
grid_size = 5

#print(range(grid_size))
#print(["0"] * 5)

for i in range(grid_size):
    board.append(["O"] * grid_size)

def print_board(board):
    for r in range(len(board)):
        print(" ".join(board[r]))

def random_row(board):
    return randint(0, len(board) -1)

def random_col(board):
    return randint(0, len(board) -1)

ship_row = random_row(board)
ship_col = random_col(board)

print_board(board)
print()
#print("ship location= %i %i" % (ship_row, ship_col))

for turn in range(5):
    print("Turn: %i" % (turn + 1))
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "X"
        print_board(board)
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(grid_size) \
         or guess_col not in range(grid_size):
            print_board(board)
            print("Oops, that's not even in the ocean.")
            print()
        elif board[guess_row][guess_col] == "X":
            board[guess_row][guess_col] = "X"
            print_board(board)
            print("You guessed that one already.")
            print()
        else:
            board[guess_row][guess_col] = "X"
            print_board(board)
            print("You missed my battleship!")
            print()

        if turn == 4:
            board[ship_row][ship_col] = "B"
            print_board(board)
            print("Battleship was at grid: %i,%i" % (ship_row, ship_col))
            print("Game Over")
