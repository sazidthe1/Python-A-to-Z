# This is Chess Dictionary Validator Project

def isValidChessBoard(board):
    # Counters for pieces
    black_king = 0
    white_king = 0
    black_pieces = 0
    white_pieces = 0
    black_pawns = 0
    white_pawns = 0

    # Valid board positions
    valid_positions = [f"{i}{j}" for i in '12345678' for j in 'abcdefgh']

    # Piece types
    piece_types = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for position, piece in board.items():
        # Check if the piece is on a valid position
        if position not in valid_positions:
            return False
        
        # Check if the piece name starts with 'w' or 'b'
        if piece[0] not in ['w', 'b']:
            return False
        
        # Check if the piece type is valid
        if piece[1:] not in piece_types:
            return False

        # Count pieces and kings
        if piece == 'bking':
            black_king += 1
        elif piece == 'wking':
            white_king += 1

        if piece[0] == 'b':
            black_pieces += 1
            if piece == 'bpawn':
                black_pawns += 1
        else:
            white_pieces += 1
            if piece == 'wpawn':
                white_pawns += 1

    # Check if there is exactly one black and one white king
    if black_king != 1 or white_king != 1:
        return False

    # Check if pieces are within limits
    if black_pieces > 16 or white_pieces > 16 or black_pawns > 8 or white_pawns > 8:
        return False

    return True

# Example chess board dictionary
example_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'
}

# Check the validity of the chess board
is_valid_board = isValidChessBoard(example_board)
print("Is the example board valid?", is_valid_board)  # Output: True or False based on the validity of the board