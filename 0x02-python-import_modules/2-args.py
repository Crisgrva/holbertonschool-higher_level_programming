#!/usr/bin/python3
import sys

argvlen = len(sys.argv)

if argvlen == 2:
    nargv = " argument:"
else:
    nargv = " arguments:"

print("{:d}".format(len(sys.argv) - 1) + nargv)

for arguments in range(1, argvlen):
    print("{:d}: {}".format(arguments, sys.argv[arguments]))
