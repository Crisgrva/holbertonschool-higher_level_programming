#!/usr/bin/python3
"""
7. Load, add, save
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename="add_item.json"):
    """
    Write a script that adds all arguments to a
    Python list, and then save them to a file:
    """
    try:
        JSON_file = load_from_json_file(filename)
    except FileNotFoundError:
        JSON_file = list()

    for item in sys.argv[1:]:
        JSON_file.append(item)

    save_to_json_file(JSON_file, filename)


add_item()
