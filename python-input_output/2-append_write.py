#!/usr/bin/python3
"""
A function to append new string at the end of text file
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
