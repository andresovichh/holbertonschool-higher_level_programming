#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def EmptyList(self):
        self.assertEqual(max_integer[None], None)

    def negnum(self):
        self.assertEqual(max_integer[-3, 2], 2)