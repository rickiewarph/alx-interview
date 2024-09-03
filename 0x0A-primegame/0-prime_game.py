#!/usr/bin/python3
"""Module to perform the Prime Game"""


def isWinner(x, nums):
    """
    Determines winner of a set of prime no.s removal games.

    Args:
        x (int): The no. of rounds.
        nums (list of int): A list of ints where each int n denotes
        a set of consecutive ints starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Initialize scores and array of possible prime no.s
    ben = 0
    maria = 0
    # Create a list 'a' of len sorted(nums)[-1] + 1 with all elements
    # initialized to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # The first two elments of the list, a[0] and a[1], are set to 0
    # because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0
    # Use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # Play each round of the game
    for i in nums:
        # If the sum of prime no.s in the set is even, Ben wins
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Removal of multiples of a prime no.s from an array of possible prime
    numbers.

    Args:
        ls (list of int): An array of possible prime no.s.
        x (int): The prime no.s to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop iterates over multiples of a prime no.s and marks them as
    # non-prime by setting a corresponding value to 0 in the input
    # list ls. Starting from 2, it sets every multiple of x up to the
    # length of ls to 0. If the index i * x is out of range for the list ls,
    # the try block will raise an IndexError exception, and the loop will
    # terminate using the break statement.
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
