#!/usr/bin/python3
"""
This is for a square. and not a circle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return(self.__width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width or self.height))

    def update(self, *args, **kwargs):
        """\_:|_/"""
        attribute = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attribute, args):
                setattr(self, attr, value)
        for key, value in kwargs.items():
            setattr(self, key, value)
