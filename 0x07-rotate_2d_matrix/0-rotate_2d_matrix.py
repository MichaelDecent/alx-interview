#!/usr/bin/python3
"""A Module that contains a function
Rotates 2D Matrix by 90 degrees
"""
from typing import List


def rotate_2d_matrix(matrix: List[list]) -> None:
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
