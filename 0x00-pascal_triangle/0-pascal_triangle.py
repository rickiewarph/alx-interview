#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of ints
    representing the Pascal Tri of n
    returns empty list if n <= 0
    """
    j = []
    if n <= 0:
        return j
    j = [[1]]
    for m in range(1, n):
        tmp = [1]
        for n in range(len(j[m - 1]) - 1):
            curr = j[m - 1]
            tmp.append(j[m - 1][n] + j[m - 1][n + 1])
        tmp.append(1)
        j.append(tmp)
    return j
