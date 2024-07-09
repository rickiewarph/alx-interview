#!/usr/bin/python3
""" Script computing min operations
    required in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method to compute the min no.
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the ops
    Return: the sum of the ops
    """
    if n < 2:
        return 0
    factor_list = []
    r = 1
    while n != 1:
        r += 1
        if n % r == 0:
            while n % r == 0:
                n /= r
                factor_list.append(r)
    return sum(factor_list)
