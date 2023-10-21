#!/usr/bin/env python3
""" This module contention the tests with unittest"""
import unittest
import parameterized
from typing import Mapping
from utils import access_nested_map


class TestAccessNetedMap(unittest.TestCase):
    """ This class check and create test of the utils functions """

    @parameterized.expand(
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b")
    )
    def test_access_nested_map(self):
        """ This function check an test the access nested map is correct"""
        nested = {"a": {"h": {"t": 11}}}
        path = ["a", "h", "t", "z"]
        self.assertEqual(Mapping, access_nested_map(nested, path))
