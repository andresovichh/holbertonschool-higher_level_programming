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
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([-2, 0, 1]), 1)
        self.assertEqual(max_integer([-2, -3, -4]), -2)
        self.assertEqual(max_integer([-2, -1, -3]), -1)
        self.assertEqual(max_integer([]), None)
