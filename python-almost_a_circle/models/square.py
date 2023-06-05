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
        if args and len(args) > 0:
            for index, value in enumerate(args):
                if index < len(attribute):
                    if attribute[index] == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, attribute[index], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, key, value)
        
    def to_dictionary(self):
        """returns the square in a dictionary form"""
        return {
            'id': self.id,
            'width': self.size,
            'x': self.x,
            'y': self.y
        }
