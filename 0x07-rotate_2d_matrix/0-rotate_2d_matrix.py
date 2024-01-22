#!/usr/bin/python3
"""Reversing a 2-d matrix clockwise 90 degrees"""


def rotate_2d_matrix(matrix):
    """
    check matrix to have 2 dimensions and will not be empty
    Transpose the matrix then reverse each row in the matrix
    - matrix - list of lists
    return nothing. rotate in place
    """
    if isinstance(matrix, list) and all(isinstance(row, list)
                                        for row in matrix):
        if matrix and all(row for row in matrix):
            matrix[:] = [list(row) for row in zip(*matrix)]
            for row in matrix:
                row.reverse()
