#!/usr/bin/python3
"""
This module defines a function to create Pascals triangle
"""


def pascal_triangle(n):
    """
    Returns pascals triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for level in range(1, n):
        previous_level = triangle[-1]
        current_level = [1]

        for i in range(1, level):
            current_level.append(previous_level[i - 1] + previous_level[i])

        current_level.append(1)
        triangle.append(current_level)

    return triangle
