#!/usr/bin/python3
"""
14. Log parsing
"""

import signal
from sys import stdin, exit

filesize = 0
count = 0
y = 0
new_list = []
stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }


def signal_handler(sig, frame):
    """
    signal handler
    """
    print("File size: {}".format(filesize))
    exit(0)


def print_line(lista=[], stats={}, rlly_filesize=0):
    """
    print lines
    """
    for x in lista[-10:]:
        status_code = x.split()[-2]
        if status_code in stats.keys():
            stats[status_code] += 1

    for key in stats:
        if stats[key] != 0:
            print("{}: {}".format(key, stats[key]))
    print("File size: {}".format(rlly_filesize))


def initializer():
    """
    drive programm
    """
    while True:
        filesize = 0
        y = 0
        for line in stdin:
            new_list.append(line)
            filesize += int(line.split()[-1])
            y += 1
            if y == 10:
                print_line(new_list, stats, filesize)
                y = 0
                break

        signal.signal(signal.SIGINT, signal_handler)


if not stdin.isatty():
    initializer()
