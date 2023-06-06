#!/usr/bin/python3
"""
Unittest module for Base class.
"""
import unittest
from models.base import Base as Base
from models.rectangle import Rectangle as Rectangle
from models.square import Square as Square


class BaseTests(unittest.TestCase):
    """
    Tests for base class
    """
    @classmethod
    def setUpClass(cls):
        """making the class' for testing"""
        cls.base1 = Base()
        cls.rectangle1 = Rectangle(1, 2, 0, 0, 100)
        cls.square1 = Square(2, 0, 0, 200)

    def delClass(cls):
        """deletes the test class'"""
        del cls.base1
        del cls.rectangle1
        del cls.square1
        return super().delClass()

    def test_init(self):
        """
        Method for testing initialization of the base class
        """
        self.assertEqual(self.base1.id, 1)

        self.base2 = Base(2)
        self.assertEqual(self.base2.id, 2)

        self.base3 = Base()
        self.assertEqual(self.base3.id, 2)

        self.assertEqual(self.base2.id, self.base3.id)

        del self.base2
        del self.base3
        
    def test_to_json_string(self):
        """
        Method for testing the json string creation
        """
        dictionary_r = self.rect1.to_dictionary()
        json_dictionary_r = self.rect1.to_json_string([dictionary_r])
        dicStr = '[{"x": 0, "y": 0, "id": 100, "height": 1, "width": 2}]'
        self.assertEqual(json_dictionary_r, dicStr)

        dictionary_s = self.square1.to_dictionary()
        json_dictionary_s = self.square1.to_json_string([dictionary_s])
        dicStr = '[{"id": 200, "x": 0, "size": 2, "y": 0}]'
        self.assertEqual(json_dictionary_s, dicStr)

        self.assertRaises(TypeError, self.square1.to_json_string, dictionary_s)
        self.assertRaises(TypeError, self.square1.to_json_string, [1])

        dicList = [self.square1.to_dictionary(), self.rect1.to_dictionary()]
        dicStr = '[{"id": 100, "x": 0, "size": 2, "y": 0}, ' \
            + '{"x": 0, "y": 0, "id": 200, "height": 1, "width": 1}]'
        self.assertEqual(self.square1.to_json_string(dicList), dicStr)

        self.assertEqual(self.square1.to_json_string(None), "[]")
        self.assertEqual(self.square1.to_json_string([]), "[]")
