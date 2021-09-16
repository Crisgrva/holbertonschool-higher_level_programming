#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {
           "I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000,
           }
    result = 0
    fst_num = romans.get(roman_string[0])
    for x in range(len(roman_string)):
        if fst_num < int(romans.get(roman_string[x])):
            result = romans.get(roman_string[x]) - result
        else:
            result += romans.get(roman_string[x])
    return result
