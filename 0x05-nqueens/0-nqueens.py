#!/usr/bin/python3
"""
This Module contain functions that handle the Nqueens Puzzle
"""
import sys


def is_safe(board, row, col, N):
    """checks if it's safe to place a queen at a specific position
    row, col) on the chessboard (board) of size N.
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """
    Prints a visual representation of the chessboard configuration,\
    """
    result = [[i, board[i]] for i in range(len(board))]
    print(result)


def solve_nqueens(N):
    """
    initializes the chessboard and starts the process of
    solving the N Queens problem. It calls the utility
    function solve_util to find and print solutions
    """
    board = [-1] * N
    solve_util(N, 0, board)


def solve_util(N, row, board):
    """
    tries to place queens on the chessboard one row at a time.
    It backtracks if a solution cannot be found
    for a specific configuration.
    """
    if row == N:
        print_solution(board)
        print()
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_util(N, row + 1, board)
            board[row] = -1


def main():
    """
    The main function of the program. It handles command-line arguments,
    checks their validity, and initiates the solving process
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
