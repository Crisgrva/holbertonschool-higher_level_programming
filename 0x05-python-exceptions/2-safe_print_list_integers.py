#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0

    for num in my_list[:x]:
        try:
            print("{:d}".format(num), end="")
            count += 1
        except (TypeError, ValueError):
            continue

    print()
    return count
