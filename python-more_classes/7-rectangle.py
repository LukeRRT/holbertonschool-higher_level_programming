#!/usr/bin/python3
"""
This module is to define a rectangle
"""


class Rectangle:
    """Class defining a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_lines = [str(self.print_symbol) * self.__width] \
            * self.__height
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Destructor that prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
