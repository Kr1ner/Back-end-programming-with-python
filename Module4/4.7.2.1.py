import math
import random
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        for item in row:
            print(item,end="|")
        print("\n")
        print("-"*5,sep="  ")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    usermove = int(input("what your move:"))
    while "X" == board[round(usermove/3)-1][usermove%3-1]:
        print("taken")
        usermove = int(input("what your move:"))
    board[math.ceil(usermove/3.0)-1][usermove%3-1] = "O"


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list = []
    row=0
    for rows in board:
        col = 0
        for item in rows:
            if item!="X" and item!="O":
                free_list.append((row,col))
            col+=1
        row+=1
    return free_list


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    return 0


def draw_move(board):
    # The function draws the computer's move and updates the board.
    computer_move = random.choice(make_list_of_free_fields(board))
    print(computer_move)


board=[[1,2,3],[4,'X',6],[7,8,9]]

display_board(board)
enter_move(board)
display_board(board)
draw_move(board)