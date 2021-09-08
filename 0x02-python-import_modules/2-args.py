#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argvlen = len(sys.argv)

    if argvlen == 2:
        nargv = " argument:"
    elif argvlen == 1:
        nargv = " arguments."
    else:
        nargv = " arguments:"

    print("{:d}".format(len(sys.argv) - 1) + nargv)

    for arguments in range(1, argvlen):
        print("{:d}: {}".format(arguments, sys.argv[arguments]))
