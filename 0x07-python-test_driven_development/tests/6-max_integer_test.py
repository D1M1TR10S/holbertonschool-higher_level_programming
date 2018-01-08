#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_emptylist(self):
        list1 = []
        self.assertEqual(max_integer(list1), None)

    def test_negatives(self):
        list1 = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list1), -1)

    def test_samevalues(self):
        list1 = [2, 2, 2, 2, 2]
        self.assertEqual(max_integer(list1), 2)

    def test_output(self):
        list1 = [1, 0, -40, 88, 32, -3.5]
        self.assertEqual(max_integer(list1), 88)

    def test_notalist(self):
        list1 = "String"
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test_string(self):
        list1 = [2, 59, "String", -8]
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test_float(self):
        list1 = [5, 12, 4.0732, 3]
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test_noparam(self):
        with self.assertRaises(TypeError):
            max_integer()

    def test_dictionary(self):
        list1 = {1:2, 3:4, 5:6}
        with self.assertRaises(TypeError):
            max_integer(list1)
