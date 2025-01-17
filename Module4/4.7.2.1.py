def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    return 0


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    return 0


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    return 0


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    return 0


def draw_move(board):
    # The function draws the computer's move and updates the board.
    return 0


board = [
    ['1','2','3'],
    ['4', 'X', '6'],
    ['7', '8', '9']
]
for i in range(0,3):
    for j in range(0,3):
        board[i][j]=(i+1)*(j+1)
print(board)