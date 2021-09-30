#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

my_square = Rectangle.square(10)
print("{} / {}".format(my_square.width, my_square.height))

my_square = Rectangle.square(2)
print("{} / {}".format(my_square.width, my_square.height))

try:
    my_square = Rectangle.square(-2)
    print("{} / {}".format(my_square.width, my_square.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_square = Rectangle.square("12")
    print("{} / {}".format(my_square.width, my_square.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
