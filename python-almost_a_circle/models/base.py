#!/usr/bin/python3
"""This class will be the base of all other classes in this project"""


class Base:
    """This is the base class"""
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # if id is not provided
            self.id = Base.__nb_objects
