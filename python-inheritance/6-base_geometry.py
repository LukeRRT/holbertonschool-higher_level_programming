#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class with a method to calculate the area.
    Methods:
    area(self): Raises an Exception with the message
    "area() is not implemented".
    """
    def area(self):
        """
        Public instance method to calculate the area.
        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")
