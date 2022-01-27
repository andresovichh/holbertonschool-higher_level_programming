#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

from typing import Type
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        """ something """
        self.assertEqual(max_integer([2, 1250, 4810, 894, 154, 1564]), 4810)

    def test_max(self):
        """ something negative """
        self.assertEqual(max_integer([2, 1250, -4810, 894, 154, 1564]), 1564)

    def test_max(self):
        """ all negative """
        self.assertEqual(max_integer([-2, -1250, -4810, -894, -154, -1564]), -2)

    def test_max(self):
        """ all negative """
        self.assertEqual(max_integer([-2, -1250, -4810, -894, -154, -1564]), -2)
    
    def test_max(self):
        """ all negative """
        self.assertEqual(max_integer([]), None)
