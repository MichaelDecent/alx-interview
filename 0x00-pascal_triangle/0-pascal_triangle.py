#!/usr/bin/python3
"""
This Module contains a functionthat returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        prev_row = pascal_triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        pascal_triangle.append(new_row)

    return pascal_triangle
