#!/usr/bin/python3
"""
2. First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    Write the class Rectangle that inherits from Base:
    """

    int_error = "must be an integer"
    greater_0_error = "must be > 0"
    geater_or_iqual_0_error = "must be >= 0"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method fot width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if isinstance(value, bool):
            raise TypeError("width " + Rectangle.int_error)
        if not isinstance(value, int):
            raise TypeError("width " + Rectangle.int_error)

        if value <= 0:
            raise ValueError("width " + Rectangle.greater_0_error)

        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method for height"""
        if isinstance(value, bool):
            raise TypeError("height " + Rectangle.int_error)
        if not isinstance(value, int):
            raise TypeError("height " + Rectangle.int_error)

        if value <= 0:
            raise ValueError("height " + Rectangle.greater_0_error)

        self.__height = value

    @property
    def x(self):
        """Getter for X"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter Method for X"""
        if isinstance(value, bool):
            raise TypeError("x " + Rectangle.int_error)
        if not isinstance(value, int):
            raise TypeError("x " + Rectangle.int_error)

        if value < 0:
            raise ValueError("x " + Rectangle.geater_or_iqual_0_error)

        self.__x = value

    @property
    def y(self):
        """Getter for Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter Method for Y"""
        if isinstance(value, bool):
            raise TypeError("y " + Rectangle.int_error)
        if not isinstance(value, int):
            raise TypeError("y " + Rectangle.int_error)

        if value < 0:
            raise ValueError("y " + Rectangle.geater_or_iqual_0_error)

        self.__y = value

    def area(self):
        """Area method"""
        return self.__height * self.__width
