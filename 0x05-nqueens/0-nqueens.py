#!/usr/bin/env python3
"""
Solve the N-Queens problem using backtracking
"""
import sys


def solve_nqueens(N):
    """
    Solves the N-Queens problem for a given board size N
    """
    def backtrack(row, cols, diag1, diag2, solution):
        """
        Recursively attempts to place queens on the board
        while avoiding conflicts using backtracking
        """
        if row == N:
            results.append(solution.copy())
            return
        for col in range(N):
            if not cols[col] and not diag1[row + col] and not diag2[row - col]:
                cols[col] = diag1[row + col] = diag2[row - col] = True
                solution.append([row, col])
                backtrack(row + 1, cols, diag1, diag2, solution)
                solution.pop()
                cols[col] = diag1[row + col] = diag2[row - col] = False

    results = []
    cols = [False] * N
    diag1 = [False] * (2 * N - 1)
    diag2 = [False] * (2 * N - 1)
    backtrack(0, cols, diag1, diag2, [])

    for result in results:
        print(result)


def validate_input():
    """
    Validates the command-line input to ensure it meets the requirements
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

    return N


if __name__ == "__main__":
    N = validate_input()
    solve_nqueens(N)
