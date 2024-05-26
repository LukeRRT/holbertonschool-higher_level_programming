#!/usr/bin/python3
"""
Module to check subclass
"""

def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited (directly or indirectly), otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
