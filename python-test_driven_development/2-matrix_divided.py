#!/usr/bin/python3
"""
This module contains function matrix_divided for dividing
all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements in a matrix

    Args:
        matrix (array): a two dimensional matrix of integers or floats
        div (int): the divisor

    Return:
        array: an array with same dimension as matrix, with each element
        divided by the divisor
    """

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError(
            "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
