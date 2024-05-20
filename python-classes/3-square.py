#!/usr/bin/python3
'''A class Square that defines a square '''


class Square:
    ''' Contains a private instance variable (also called attribute: size)'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
