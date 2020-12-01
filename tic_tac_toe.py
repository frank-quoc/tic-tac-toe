import time
from random import randint

from board import new_board, print_board

def instructions():
    """Displays how to to play the game and the rules."""
    print('''WELCOME TO TIC-TAC-TOE! You will be playing the game against a computer. 
Moves can be made by inputting the numbers 1-9 and are representing each space in the board like this:
7|8|9
-+-+-
4|5|6
-+-+-
1|2|3 
The games is over when the either the player or computer gets 3 in a row, column, or diagonally.\n''')

def x_or_o():
    """Player picks 'X' or 'O'. Computer will be the other choice"""
    while True:
        # Player picks if they want to be 'X' or 'O'
        player = input("Do you want to be 'X' or 'O'? ").upper()
        if player != 'X' and player != 'O':
            print("You did not pick a valid entry, please try again.")
            continue
        if player == 'X':
            computer = 'O'
        else:
            computer = 'X'
        return player, computer

# The first player is picked.
def pick_first_player(human, computer):
    """Chooses who goes first."""
    print("Flipping a coin...")
    first_player = randint(0, 1)
    if first_player == 0:
        print("Human player gets to go first.\n")
        return human
    else:
        print("I, the computer, get to go first.\n")
        return computer

def human_move(board):
    """Receives input from the player to input into the square."""
    while True:
        player_move = int(input("Pick a number between 1-9 to place your move on the board: "))
        if player_move not in range(1, 10):
            print("Not a valid input. Choose a number between 1-9.")
            continue
        if board[player_move] != ' ':
            print(f"The {player_move} square already has a {board[player_move]}.")
            continue
        else:
            print("Player turn...")
            return player_move

def comp_move(board, computer, human):
    """Instructions for the computer to fill in a square."""
    print("Computer turn...")
    time.sleep(1.5)
    # Searches for the best available move for the computer to win.
    for k, v in board.items():
        if v != " ":
            continue
        hold_val = board[k]
        board[k] = computer
        if winner(board) == computer:
            comp_move = k
            return comp_move
        board[k] = hold_val # if the choices didn't result in a computer win  
    # Searches for the best available move to block the player from winning.
    for k, v in board.items():
        if v != " ":
            continue
        hold_val = board[k]
        board[k] = human
        if winner(board) == human:
            comp_move = k
            return comp_move
        board[k] = hold_val
    # Otherwise, just pick a random square.
    while True:
        comp_move = randint(1, 9)
        if board[comp_move] != " ":
            continue
        return comp_move

def winner(board):
    """Checks win conditions."""
    WIN_COND = ((7, 8, 9), (4, 5, 6), (1, 2 ,3), # Horizontal Wins
                (7, 4, 1), (8, 5, 2), (9, 6, 3), # Vertical Wins
                (7, 5, 3), (1, 5, 9)) # Diagonal Wins
    for i in WIN_COND:
        if board[i[0]] == board[i[1]] == board[i[2]] != " ":
            return board[i[0]]
    else: 
        return False

def restart():
    again = input("\nWould you like to start again? (y/n) ").lower()
    print()
    if again != 'y':
        exit()
    else:
        main()

def main():
    moves = 0
    instructions()
    human, computer = x_or_o()
    curr_player = pick_first_player(human, computer)
    board = new_board()

    while moves < 9:
        if curr_player == human:
            board[human_move(board)] = human
            curr_player = computer
            print_board(board)
            # Check to see if there's a winner after 5 moves.
            if moves >= 5:
                if winner(board) == human:
                    print("GAME OVER! You have bested me this time, Player.")
                    break
        else:
            board[comp_move(board, computer, human)] = computer
            curr_player = human
            print_board(board)
            if moves >= 5:
                if winner(board) == computer:
                    print("MWHAHAHA! Computers have taken over the world.")
                    break
        moves += 1
    if moves == 9:
        print("TIE! We are of equal intelligence.")
    restart()

if __name__ == '__main__':
    main()