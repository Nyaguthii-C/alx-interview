#!/usr/bin/python3
"""A function that prints the pascal triangle"""


def pascal_triangle(n):
    """
    Args: number of rows in Pascal's triangle
    Return: list of lists of integers representing the Pascal’s triangle of n
    """

    """Return empty list if no number of rows specified"""
    try:
        if not isinstance(n, int):
            raise TypeError("n must be an integer")

        if int(n) <= 0:
            return [[]]

    #   initial row
        elif int(n) == 1:
            return [[1]]

    #   Add row with coefficients depending on row number"""
        else:
            """ Default second row value"""
            Triangle = [[1], [1, 1]]

            for i in range(2, n):
                """calculate coefficients in  new row based on previous row"""
                add_row = [1] + [
                    Triangle[-1][j-1] + Triangle[-1][j] for j in range(1, i)
                ] + [1]
                Triangle.append(add_row)

            return Triangle
    # handle instance where n is passed as an non-integer value
    except TypeError as e:
        print(e)
        return [[]]
