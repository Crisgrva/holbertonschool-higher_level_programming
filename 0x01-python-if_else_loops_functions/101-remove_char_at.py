#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    newStr = str[:n] + str[n+1:]
    return newStr
