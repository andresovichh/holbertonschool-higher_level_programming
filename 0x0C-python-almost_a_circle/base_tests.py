#!/usr/bin/python3
  
"""Unittest for the Base class"""
import unittest
from models.base import Base
import pep8


"""
Tests for the Base CLASS
 """


class TestBase(unittest.TestCase):

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Base.__doc__) > 0)
    
    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(Base.__init__.__doc__) > 0)



    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['base.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")

    #def test_ 
if __name__ == "__main__":
    unittest.main()