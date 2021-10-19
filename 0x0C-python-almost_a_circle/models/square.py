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
