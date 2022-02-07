#!/usr/bin/python3
  
"""Unittest for the Base class"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8
import os


"""
Tests for the Base CLASS
 """


class TestBase(unittest.TestCase):

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)
    
    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_documentations1(self):
        """check if method has doc"""

        self.assertTrue(len(Rectangle.area.__doc__) > 0)
    
    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(Rectangle.display.__doc__) > 0)
    
    def test_documentations3(self):
        """check if method has doc"""

        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)
    
    def test_documentations4(self):
        """check if method has doc"""

        self.assertTrue(len(Rectangle.update.__doc__) > 0)    

# 1 Test if same result as intranet
    def test_Rectanglecreation(self):
        """ as per itnranet"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_toomanyargs(self):
        """ too many args test"""
        Base._Base__nb_objects = 0

        
        errm = "TypeError: __init__() takes from 3 to 6 positional arguments but 7 were given"
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1, 2, 3, 4, 5, 6)
            self.assertEqual(errm, str(err.exception))

    def test_noargs(self):
        """ no args test"""
        Base._Base__nb_objects = 0
        errm = "TypeError: __init__() takes from 3 to 6 positional arguments but 7 were given"
        with self.assertRaises(TypeError):
            rec4t = Rectangle()
    
    def test_a_string(self):
        """ no args test"""
        Base._Base__nb_objects = 0
        errm = "TypeError: __init__() takes from 3 to 6 positional arguments but 7 were given"
        with self.assertRaises(TypeError):
            rec4t = Rectangle(10, "30")


    def test_Noheight(self):
        """ Height as string"""
        err = "[TypeError] height must be an integer"

        try:
            Rectangle(10, "2")
        except Exception as e:
            mess = "[{}] {}".format(e.__class__.__name__, e)

        self.assertEqual(mess, err)

    def test_negativewidth(self):
        """ negative width"""
        err = "[ValueError] y must be >= 0"
        try:
            r = Rectangle(10, 2, 3, -1)

        except Exception as e:
            mess = "[{}] {}".format(e.__class__.__name__, e)

        self.assertEqual(err, mess)

    def test_area(self):
        """ test area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_str__(self):
        """ test __str__ method"""
        Base._Base__nb_objects = 0

        r1 = Rectangle(4, 6, 2, 1, 12)
        msg = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), str(msg))

class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)