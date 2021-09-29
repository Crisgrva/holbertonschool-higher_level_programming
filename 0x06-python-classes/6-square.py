#!/usr/bin/python3
"""3. Area of a square"""


class Square:
    """Write a class Square that defines a square by:
    (based on 2-square.py)
    """
    def __init__(self, size=0, position=(0, 0)):
        ispx = isinstance(position[0], int)
        ispy = isinstance(position[1], int)

        if isinstance(size, int) is False:
            raise Exception("size must be an integer")
        elif size < 0:
            raise Exception("size must be >= 0")

        if ispx is False or ispy is False:
            raise Exception("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")

        self.__position = position
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def my_print(self):
        position = self.__position
        x = position[0]
        y = position[1]

        px = 0
        py = 0
        spcy = " " * (y - 1)

        if self.__size == 0:
            print()
        if y > 0:
            for stls in range(0, y):
                print("{}".format(spcy))
        for px in range(0, self.__size):
            print("{}".format(" " * x), end="")
            for py in range(0, self.__size):
                print("#", end="")
            print()
