#!/usr/bin/env python3
"""
A class named CountedIterator that wraps around an iterator
and keeps count of the number of items retrieved.
"""


class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items")
