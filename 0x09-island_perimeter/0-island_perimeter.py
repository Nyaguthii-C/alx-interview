#!/usr/bin/python3
"""Function that returns island perimeter"""


def island_perimeter(grid):
    """
    Args:
       grid  - list of lists of integers , 1 and 0
             - 0 represents water
             - 1 represents land
             - Each cell is square, with a side length of 1
             - Cells are connected horizontally/vertically (not diagonally).
             - grid is rectangular, width and height not exceeding 100
    Returns :
       perimeter - int
    """
    islands = 0
    adjacentIsland = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                islands += 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    adjacentIsland += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    adjacentIsland += 1
    return 4 * islands - 2 * adjacentIsland
