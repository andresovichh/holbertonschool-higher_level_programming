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
    def test_usual_case(self):
        """ Basic test case"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(-200)
        self.assertEqual(b3.id, -200)
    
    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(Base.__init__.__doc__) > 0)




class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        # """Test that we conform to PEP8."""
        # pep8style = pep8.StyleGuide(quiet=True)
        # result = pep8style.check_files(['base.py'])
        # print(result)
        # self.assertEqual(result.total_errors, 0,
        #                  "Found code style errors (and warnings).")
        # https://pep8.readthedocs.io/en/release-1.7.x/intro.html
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)


if __name__ == "__main__":
    unittest.main()