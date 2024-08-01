#!/usr/bin/python3
"""
Sln to the nqueens problem
"""
import sys


def backtrack(v, n, cols, pos, neg, board):
    """
    backtrack func to find solution
    """
    if v == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (v + c) in pos or (v - c) in neg:
            continue

        cols.add(c)
        pos.add(v + c)
        neg.add(v - c)
        board[v][c] = 1

        backtrack(v+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(v + c)
        neg.remove(v - c)
        board[v][c] = 0


def nqueens(n):
    """
    Sln to nqueens problem
    Args:
        n (int): no. of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
