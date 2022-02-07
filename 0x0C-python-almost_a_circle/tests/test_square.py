#!/usr/bin/python3
""" module that tests Square"""
import json
import unittest
from models.square import Square
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


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)