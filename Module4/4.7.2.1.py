import math
import random

def display_board(board):
    # Prints the board in a cleaner format
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        printrow = "|"+ "|".join(str(item).center(7) for item in row)+ "|"
        print(f"{printrow:>25}")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user for their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            usermove = int(input("What's your move (1-9): "))
            if usermove < 1 or usermove > 9:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue

            row = (usermove - 1) // 3
            col = (usermove - 1) % 3

            if board[row][col] != 'X' and board[row][col] != 'O':
                board[row][col] = 'O'
                break
            else:
                print("This spot is already taken, try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def make_list_of_free_fields(board):
    # Returns a list of tuples representing free fields (empty spots) on the board
    free_list = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' and board[row][col] != 'O':
                free_list.append((row, col))
    return free_list

def victory_for(board, sign):
    # This function checks for a victory (row, column, or diagonal)
    # Check rows
    for row in range(3):
        if all([board[row][col] == sign for col in range(3)]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == sign for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == sign for i in range(3)]) or all([board[i][2 - i] == sign for i in range(3)]):
        return True

    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    computer_move = random.choice(make_list_of_free_fields(board))
    row, col = computer_move
    board[row][col] = 'X'

# Initialize the board
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

def game_loop():
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)

        draw_move(board)
        display_board(board)

        if victory_for(board, 'O'):
            print("You win!")
            return
        elif victory_for(board, 'X'):
            print("Computer wins!")
            return
        elif not make_list_of_free_fields(board):
            print("Its A tie!")
            return
game_loop()