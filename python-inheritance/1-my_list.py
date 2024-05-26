#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """class MyList inherited from list"""
    
    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
