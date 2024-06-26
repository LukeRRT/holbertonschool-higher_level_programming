#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list,
and then saves them to a file named add_item.json.

It uses the functions save_to_json_file and load_from_json_file
for handling JSON data.
"""
import sys
import os


# Import the functions from the respective files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items if the file exists, otherwise create an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
