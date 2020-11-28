import random

board = {   7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '  }

def print_board():
    """Prints the current board."""
    print( board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print( board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print( board[1] + '|' + board[2] + '|' + board[3])

def x_or_o():
    """Player picks 'X' or 'O.' The first player is randomly picked."""
    while True:
        # Player picks if they want to be 'X' or 'O'
        player_choice = input("Do you want to be 'X' or 'O'? ")
        if player_choice != 'X' and player_choice != 'O':
            print("You did not pick a valid entry, please try again.")
            continue
        return player_choice

# # The first player is picked.
# print("Flipping a coin...")
# first_player = random.randint(0, 1)
# if first_player == 0:
#     return player_choice
# else:
#     return computer

def move():
    moves = 0
    player_choice = x_or_o()
    # Sets the player to their choice and the computer to the other choice.
    if player_choice == 'X':
        computer = 'O'
    else:
        computer = 'X'
    while moves < 10:
        flag = True
        player_turn = int(input("Pick a number between 1-9 to place your move on the board: "))
        if board[player_turn] != ' ':
            print(f"The {player_turn} square already has a {board[player_turn]}.")
            continue
        else:
            board[player_turn] = player_choice
            moves += 1
            while flag:
                computer_turn = random.randint(1, 9)
                if board[computer_turn] != ' ':
                    continue
                else:
                    board[computer_turn] = computer
                    flag = False
        print_board()

if __name__ == '__main__':
    move()