#!/usr/bin/python3
"""
a function to return JSON representation by Python data
structure
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string."""
    return json.loads(my_str)
