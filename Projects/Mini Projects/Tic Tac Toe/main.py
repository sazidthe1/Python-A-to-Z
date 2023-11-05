# Creating the board
board = ['-', '-', '-'
         '-', '-', '-'
         '-', '-', '-']


def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def play_game():
    # Displaying initial board
    display_board()
    handle_turn()

def handle_turn():
    position = input('Choose a position from 1-9: ')
    position = int(position) -1
    board[position] = 'X'

play_game() 


# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check cloumns
    # check diagonals
# check tie
# flip player