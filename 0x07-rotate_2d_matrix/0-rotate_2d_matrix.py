#!/usr/bin/python3
"""A Module that contains a function
Rotates 2D Matrix by 90 degrees
"""


def rotate_2d_matrix(matrix) -> None:
    """Rotates 2D Matrix by 90 degrees"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #reverse each row in the matrix
    for i in range(n):
        matrix[i].reverse()
