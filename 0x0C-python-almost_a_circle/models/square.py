#!/usr/bin/python3
"""
10. And now, the Square!
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the class Square that inherits from Rectangle:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class Constructor
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__"""

        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter method for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            _id = kwargs.get("id")
            _size = kwargs.get("size")
            _x = kwargs.get("x")
            _y = kwargs.get("y")

            self.id = _id if _id is not None else self.id
            self.size = _size if _size is not None else self.size
            self.x = _x if _x is not None else self.x
            self.y = _y if _y is not None else self.y
