#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--3x3")

my_square_3 = Square(3, (3, 3))
my_square_3.my_print()

print("--")



try:
    my_square_3 = Square(3, ("asd", 0))
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")


try:
    my_square_3 = Square(3, (1, "asd"))
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")


try:
    my_square_3 = Square(3, (-10, 0))
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")

try:
    my_square_3 = Square(3, (2, -2))
    my_square_3.my_print()
except Exception as e:
    print(e)

print("--")


