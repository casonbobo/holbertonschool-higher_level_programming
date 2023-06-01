#!/usr/bin/python3
"""
Rectangle. Building from the base class
"""
from models.base import Base


class Rectangle(Base):
    """This is a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return(self.__width)

    @property
    def height(self):
        return(self.__height)

    @property
    def x(self):
        return(self.__x)

    @property
    def y(self):
        return(self.__y)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__y = value

    def area(self):
        """Area function for rectangle"""
        return(self.__height * self.__height)
