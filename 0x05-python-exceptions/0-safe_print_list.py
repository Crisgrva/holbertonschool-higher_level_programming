#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for num in my_list[:x]:
        try:
            print(num, end="")
            count += 1
        except:
            pass
    print()
    return count
