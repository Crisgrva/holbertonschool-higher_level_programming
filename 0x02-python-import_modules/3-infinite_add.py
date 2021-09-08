#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    """
    Declare Variable
    """
    argvlen = len(sys.argv)
    result = 0

    for num in range(1, argvlen):
        result += int(sys.argv[num])

    print("{:d}".format(result))
