#!/usr/bin/python3
"""
square
"""


class Square:
    """this class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return(self.__size * self.__size)

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for y in range(0, self.__position[1]):
            print("")
        for row in range(self.__size):
            for x in range(0, self.__position[0]):
                print("")
            for each in range(self.__size):
                print("#", end="")
        print("")
