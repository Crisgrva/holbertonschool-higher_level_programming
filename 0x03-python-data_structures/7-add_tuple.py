#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 2 and len(tuple_b) == 2:
        num_1 = tuple_a[0] + tuple_b[0]
        num_2 = tuple_a[1] + tuple_b[1]
        new_duple = (num_1, num_2)
        return new_duple

    if len(tuple_a) == 2 and len(tuple_b) == 1:
        num_1 = tuple_a[0] + tuple_b[0]
        num_2 = tuple_a[1]
        new_duple = (num_1, num_2)
        return new_duple

    if len(tuple_a) == 1 and len(tuple_b) == 2:
        num_1 = tuple_a[0] + tuple_b[0]
        num_2 = tuple_b[1]
        new_duple = (num_1, num_2)
        return new_duple

    if len(tuple_a) == 1 and len(tuple_b) == 1:
        num_1 = tuple_a[0] + tuple_b[0]
        new_duple = (num_1, 0)
        return new_duple

    if len(tuple_a) == 2 and len(tuple_b) == 0:
        return tuple_a

    if len(tuple_a) == 0 and len(tuple_b) == 2:
        return tuple_b

    if len(tuple_a) == 1 and len(tuple_b) == 0:
        new_duple = (tuple_a[0], 0)
        return new_duple

    if len(tuple_a) == 0 and len(tuple_b) == 1:
        new_duple = (tuple_b[0], 0)

    new_duple = (0, 0)
    return new_duple
