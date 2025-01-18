def is_valid_sudoku(board):
    def is_valid_group(group):
        return sorted(group) == list("123456789")

    for row in board:
        if not is_valid_group(row):
            return False

    for col in range(9):
        if not is_valid_group([board[row][col] for row in range(9)]):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
            if not is_valid_group(box):
                return False

    return True

sudoku = [input().strip() for _ in range(9)]
if all(len(row) == 9 and row.isdigit() for row in sudoku):
    print("Yes" if is_valid_sudoku(sudoku) else "No")
else:
    print("No")
