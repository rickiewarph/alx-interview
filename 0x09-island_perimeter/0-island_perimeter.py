#!/usr/bin/python3
"""To define island perimeter finding func."""


def island_perimeter(grid):
    """Return perimiter of an island.
    The grid representing water by 0 and land by 1.
    Args:
        grid (list): A list of list of ints representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for m in range(height):
        for j in range(width):
            if grid[m][j] == 1:
                size += 1
                if (j > 0 and grid[m][j - 1] == 1):
                    edges += 1
                if (m > 0 and grid[m - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2
