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

    @classmethod
    def load_from_file(cls):
        """Class method that Returns: A list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
