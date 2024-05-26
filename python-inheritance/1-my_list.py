#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """class MyList inherited from list"""

    def print_sorted(self):
        sorted_list = sorted(self)
        """Prints the list sorted in ascending order."""
        print(sorted_list)
