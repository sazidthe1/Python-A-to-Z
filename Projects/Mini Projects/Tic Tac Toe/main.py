# Creating the board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


# ----- Global Variables -----
# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who's turn is it?
current_player = 'X'


# Displaying the board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Playing the game of tic-tac-toe
def play_game():

    # Displaying initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # Handling a single turn of an arbitrary player
        handle_turn(current_player)

        # Checking if the game has ended
        check_if_game_over()

        # Fliping to the other player
        flip_player()

# The game has ended
if winner == 'X' or winner == 'O':
    print(winner + 'won.')
elif winner == None:
    print("Tie.")


# Handling a single turn of an arbitrary player
def handle_turn(player):
    position = input('Choose a position from 1-9: ')
    position = int(position) - 1    # Subtracting 1 to match the list index
    board[position] = 'X'   # Assuming player is always 'X'
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    
    # Setting up the global variables 
    global winner

    # checking the rows
    row_winner = check_rows()
    # checking the cloumns
    col_winner = check_columns()
    # checking the diagonals
    diag_winner = check_diagonals()

    # Getting the winner
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner == None
    return


def check_rows():
    # Setting up the global variables
    global game_still_going
    # Checking if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # Id any rows does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return 


def check_columns():
    # Setting up the global variables
    global game_still_going
    # Checking if any of the columns have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    # Id any rows does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagonals():
    # Setting up the global variables
    global game_still_going
    # Checking if any of the diagonals have all the same values (and is not empty)
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[6] == board[4] == board[2] != '-'
    # Id any rows does have a match, flag that there is a win
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return

def check_if_tie():
    return

def flip_player():
    return

play_game()