"""The game of noughts and crosses."""

def empty_board():
    """Create a new, empty board."""
    board = []
    for r in range(3):
        row = []
        for col in range(3):
            row.append(" ")
        board.append(row)
    return board

def update_board(board, pos, new_value):
    """Update the board with a move."""
    board[pos[0]][pos[1]] = new_value
    return board

def winner(board):
    """Return the winner or None."""
    # check for horizontal winners
    for row in board:
        if row[0] != ' ' and row[0] == row[1] and row[1] == row[2]:
            return row[0]
    # check for vertical winners
    for col in range(3):
        if board[0][col] != ' ' and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return board[0][col]
    # check for diagonal winner
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None

def game_over(board):
    """Return True if there is a winner."""
    w = winner(board)
    if w:
        return True
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

def print_board(board):
    """Print the board to the screen."""
    print_divider()
    for row in board:
        row_str = "| "
        for col in row:
            row_str += col
            row_str += " | "
        print(row_str)
        print_divider()

def print_divider():
    """Print a horisontal divider."""
    print(" --- --- ---")

def noughts_and_crosses():
    """Play a game of noughts and crosses."""
    b = empty_board()
    player = "X"
    while not game_over(b):
        row = int(input("Enter a row (zero-based)"))
        col = int(input("Enter a column (zero-based)"))
        b = update_board(b, (row, col), player)
        print_board(b)
        player = "O" if player == "X" else "X"
    w = winner(b)
    if w:
        print(w + " is the winner!")
    else:
        print("It was a draw")
