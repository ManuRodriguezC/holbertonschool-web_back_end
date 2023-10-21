#!/usr/bin/env python3
""" This module contention the tests with unittest"""
from unittest import TestCase
import parameterized
from typing import Mapping
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ This class check and create test of the utils functions """

    def test_access_nested_map(self):
        """ This function check an test the access nested map is correct"""
        nested = {"a": {"h": {"t": 11}}}
        path = ["a", "h", "t"]
        self.assertEqual(Mapping, access_nested_map(nested, path))
