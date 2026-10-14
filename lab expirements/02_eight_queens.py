"""
Day 1 - Program 2: 8-Queens Problem (CO1)
Solved using backtracking. Places 8 queens on an 8x8 board so that
no two queens attack each other.
"""
N = 8


def is_safe(board, row, col):
    """board[r] = column of the queen placed in row r."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(board, row, solutions):
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, solutions)
            board[row] = -1  # backtrack


def print_board(board):
    for r in range(N):
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))
    print()


if __name__ == "__main__":
    solutions = []
    solve([-1] * N, 0, solutions)

    print(f"Total solutions for {N}-Queens: {len(solutions)}\n")
    print("First solution:")
    print_board(solutions[0])
    print("Queen positions (row, col):", [(r, c) for r, c in enumerate(solutions[0])])
