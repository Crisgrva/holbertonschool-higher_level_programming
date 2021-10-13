#!/usr/bin/python3
"""
6. Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Write a function that creates an
    Object from a “JSON file”:
    """
    with open(filename, 'r') as f:
        return(json.loads(f.read()))
