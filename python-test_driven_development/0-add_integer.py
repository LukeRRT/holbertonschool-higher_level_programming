#!/usr/bin/python3
"""
add_integer: module that adds two integers together
"""


def add_integer(a, b=98):
    """
    A function that adds two integers

    Args:
        int a: The first integer to add.
        int b: The second integer to add, defaults to 98.

    Returns:
        The sum of a + b

    Raises:
        TypeError: If either a or b is not an integer.

    Unit tests: located in tests/0-add_integer.txt
    """

    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if b == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")

    if b != b:  # check for NaN
        raise ValueError("cannot convert float NaN to integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b
