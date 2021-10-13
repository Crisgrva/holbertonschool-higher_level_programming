#!/usr/bin/python3
"""
14. Log parsing
"""

import signal
from sys import stdin, exit

filesize = 0
count = 0
x = 0
y = 0
new_list = []

def signal_handler(sig, frame):
    print("File size: {}".format(filesize))
    exit(0)

def print_line(lista=[]):
    for x in lista[-10:]:
        status_code = x.split()[-2]
        print("{}".format(status_code))
    print("File size: {}".format(filesize))
    

while True:
    for line in stdin:
        new_list.append(line)
        filesize += int(line.split()[-1])
        y += 1
        if y == 10:
            print_line(new_list)
            y = 0
            break
    
    signal.signal(signal.SIGINT, signal_handler)

