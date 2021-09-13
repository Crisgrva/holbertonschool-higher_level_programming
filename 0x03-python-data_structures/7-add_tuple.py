#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    try:
        num_1 = tuple_a[0] + tuple_b[0]
    except IndexError:
        num_1 = tuple_a[0]
    except IndexError:
        num_1 = tuple_b[0]

    try:
        num_2 = tuple_a[1] + tuple_b[1]
    except IndexError:
        num_2 = tuple_a[1]
    except IndexError:
        num_2 = tuple_b[1]

    new_tuple = (num_1, num_2)
    return new_tuple
