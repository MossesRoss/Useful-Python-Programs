import numpy as np

def is_valid(board, row, col, num):
    # Check if 'num' is valid in the current row and column
    if num in board[row, :] or num in board[:, col]:
        return False

    # Check if 'num' is valid in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    subgrid = board[start_row:start_row+3, start_col:start_col+3]
    if num in subgrid:
        return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        num = str(num)
        if is_valid(board, row, col, num):
            board[row, col] = num

            if solve_sudoku(board):
                return True

            board[row, col] = '0'

    return False  # No solution found

def find_empty_cell(board):
    # Return the indices of the first empty cell
    return np.argwhere(board == '0')[0]

def print_board(board):
    for row in board:
        print(' '.join(row))

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = np.array([
    ['5', '3', '0', '0', '7', '0', '0', '0', '0'],
    ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
    ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
    ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
    ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
    ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
    ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
    ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
    ['0', '0', '0', '0', '8', '0', '0', '7', '9']
])

print("Sudoku puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSudoku solution:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
