#!/usr/bin/python3
"""
13. Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Write a function that inserts a line of text
    to a file, after each line containing a
    specific string (see example):
    """
    with open(filename, 'r') as f:
        file = f.readlines()

    new_file = ""
    for line in file:
        new_file += line
        if search_string in line:
            new_file += new_string

    with open(filename, 'w') as f:
        f.write(new_file)
