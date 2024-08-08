#!/usr/bin/python3
"""
This module contains a method to calculate the minimum number of operations
needed to result in exactly n 'H' characters in a file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    to result in exactly n 'H' characters.
    """
    if n <= 1:
        return 0

    for div in range(2, n + 1):
        if n % div == 0:
            return minOperations(n // div) + div

    return n
