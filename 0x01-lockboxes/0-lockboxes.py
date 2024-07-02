#!/usr/bin/python3

"""
Problem: You have n no. of locked bxes in front of you.
         Each bx is numbered sequentially from 0 to n - 1
         and each bx contain keys to the other bxes.
Task: Write a method determining whether all the bxes can be opened.
"""


def canUnlockAll(bxes):
    """
    Fun checking with boolean value if the list type and
    length to invoke two for iterations one to traverse the list
    and the other to compare whether key is idx or not in order to open
    """
    if type(bxes) is not list:
        return False
    elif (len(bxes)) == 0:
        return False
    for k in range(1, len(bxes) - 1):
        bxes_checked = False
        for idx in range(len(bxes)):
            bxes_checked = k in bxes[idx] and k != idx
            if bxes_checked:
                break
        if bxes_checked is False:
            return bxes_checked
    return True
