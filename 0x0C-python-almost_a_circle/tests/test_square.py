#!/usr/bin/python3
""" module that tests Square"""
import json
import unittest
from models.square import Square
from models.base import Base
import pep8

class TestBase(unittest.TestCase):

    def test_documentation(self):
        """documentation"""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(Square.__init__.__doc__) > 0)

    def test_documentations1(self):
        """check if method has doc"""

        self.assertTrue(len(Square.__str__.__doc__) > 0)
    
    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(Square.size.__doc__) > 0)
    
    def test_documentations3(self):
        """check if method has doc"""

        self.assertTrue(len(Square.width.__doc__) > 0)
    
    def test_documentations4(self):
        """check if method has doc"""

        self.assertTrue(len(Square.update.__doc__) > 0)    
    
    def test_documentation5(self):
        """documentation"""

        self.assertTrue(len(Square.to_dictionary.__doc__) > 0)


    def test_asquare(self):
        """ a single square"""
        s1 = Square(5)
        msg = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), msg)
        self.assertEqual(s1.area(), 25)
    
    def test_update(self, *args, **kwargs):
        """ test the update method"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        msg = "[Square] (1) 3/4 - 2"
        self.assertEqual(s1.__str__, msg)
        s1.update(size=7, y=1)
        mssg2 = "[Square] (1) 12/1 - 7"
        self.assertEqual(s1.__str__, mssg2)


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)
