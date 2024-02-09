#!/usr/bin/python3
"""
A Module that contains a function that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.

    Args:
        grid: A list of lists of integers, where 0 represents water and 1 represents land.

    Returns:
        The perimeter of the island in the grid.
    """

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for the sides of the land cell
                perimeter += 4

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 for shared side with neighbor

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 for shared side with neighbor

    return perimeter
