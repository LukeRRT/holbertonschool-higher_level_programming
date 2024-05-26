#!/usr/bin/python3
"""
A function that prints text with 2 new lines after each of these chars: . ? :
"""


def text_indentation(text):
    """
    Args:
        text (str): The input text.
        result = the changed text
    Raises:
        TypeError: If text is not a string.
    Prints:
        The modified text with 2 new lines after each '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
