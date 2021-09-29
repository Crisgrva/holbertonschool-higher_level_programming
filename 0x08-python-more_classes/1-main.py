#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

try:
    my_rectangle = Rectangle("asd", "asd")
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle("asd", 0)
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle(0, "asd")
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle(-1, -1)
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle(-1, 0)
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle(0, -1)
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle(0, 0)
except Exception as e:
    print(e)

try:
    my_rectangle = Rectangle(0, )
except Exception as e:
    print(e)



