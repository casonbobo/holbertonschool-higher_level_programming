#!/usr/bin/python3
"""
This is for a square. and not a circle
"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """This is a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width = size, height = size)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
