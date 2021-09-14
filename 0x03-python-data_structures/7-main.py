#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

print(add_tuple((1, 2), (3, 4)))
print(add_tuple((1, 2), (3, )))
print(add_tuple((1, 2), ()))
print(add_tuple((1, ), (3, )))
print(add_tuple((1, ), ()))
print(add_tuple((1, ), (3, 4)))
print(add_tuple((), (3, 4)))
print(add_tuple((), (3, )))
print(add_tuple((), ()))
print(add_tuple((1, 2, 3, 4), (5, 6, 7, 8)))
