#!/usr/bin/env python3
""" This module contention the tests with unittest"""
from unittest import TestCase
from parameterized import parameterized
from typing import Mapping
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ This class check and create test of the utils functions """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ This function check an test the access nested map is correct"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ This test check if the key value exist """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
