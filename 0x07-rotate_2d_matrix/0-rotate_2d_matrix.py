#!/usr/bin/python3
"""
This module rotates a matrix 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    """
    matrix_size = len(matrix)

    for row in range(matrix_size):
        for column in range(row, matrix_size):
            temp = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = temp

    for row in range(matrix_size):
        matrix[row].reverse()
