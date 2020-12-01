def new_board():
    """Sets the new board."""
    board = {   7: ' ', 8: ' ', 9: ' ',
                4: ' ', 5: ' ', 6: ' ',
                1: ' ', 2: ' ', 3: ' '  }
    return board

def print_board(board):
    """Prints the current board."""
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print()