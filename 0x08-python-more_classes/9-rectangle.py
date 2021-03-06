#!/usr/bin/python3
"""
1. Real definition of a rectangle
"""


class Rectangle:
    """Empty class Square that defines a rectangle.
    Starting to use Comments in Python
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        str_print = ""
        print_repr = str(self.print_symbol)

        if self.__width == 0 or self.__height == 0:
            return str_print
        h = 1
        while h <= self.__height:
            str_print += print_repr * self.__width
            if h < self.__height:
                str_print += "\n"
            h += 1
        return str_print

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)
        return "Rectangle(" + width + ", " + height + ")"

    @classmethod
    def square(cls, size=0):
        new_rectangle = cls(size, size)
        return new_rectangle
