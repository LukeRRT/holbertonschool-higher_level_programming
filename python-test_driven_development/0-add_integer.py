#!/usr/bin/python3
def add_integer(a, b=98):
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
