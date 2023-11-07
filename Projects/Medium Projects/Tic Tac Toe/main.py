# Creating the board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# ----- Global Variables -----

# Lets us know if the game is over yet
game_still_going = True

# Tell us who the winner is
winner = None

# Who the current player is (X goes first)
current_player = 'X'

# ------------- Functions ---------------

# Playing the game of tic-tac-toe
def play_game():

    # Displaying initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # Handling a turn
        handle_turn(current_player)

        # Checking if the game is over
        check_if_game_over()

        # Fliping to the other player
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print("Tie.")


# Displaying the board on the screen
def display_board():
    print('\n')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('\n')


# Handling a single turn of an arbitrary player
def handle_turn(player):

    # Getting position from player
    print(player + "'s turn.")
    position = input('Choose a position from 1-9: ')
    
    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Choose a position from 1-9: ')

        # Subtracting 1 to match the list index
        position = int(position) - 1    

        # Then also make sure the spot is available on the board
        if board[position] == '-':
            valid = True
        else:
            print("You can't go there. Go again.")

    # Putting the game piece on the board        
    board[position] = player

    # Showing the game board
    display_board()


# Check if the game is over
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
        winner = None

# Checking the rows for a win
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
    # Or return None if there was no winner
    else:
        return None

# Checking the columns for a win
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
    # Or return None if there was no winner
    else:
        return None
    
# Checking the diagonals for a win
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
    # Or return None if there was no winner
    else:
        return None
    
# Checking if there is a tie
def check_if_tie():
    # Setting global variables
    global game_still_going
    if '-' not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False

# Fliping the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # if the current player was X, then change it to O
    if current_player == 'X':
        current_player = 'O'
        # if the current player was O, then change it to X
    elif current_player == 'O':
        current_player = 'X'
    return

# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()