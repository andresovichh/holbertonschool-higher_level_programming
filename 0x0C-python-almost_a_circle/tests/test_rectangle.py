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
    