#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    average_mul = []
    [average_mul.append(duple[0] * duple[1]) for duple in my_list]
    average_mul = sum(average_mul)

    divisor = 0
    for duple in my_list:
        divisor += duple[1]

    return average_mul/divisor
