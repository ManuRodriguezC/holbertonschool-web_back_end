#!/usr/bin/env python3
"""This module inherits from basecaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class creates caches by inheriting
    the cahe_data dictionary in which the cahe
    data will be saved using a key and a value,
    so that it can be accessed at any time.
    """

    def put(self, key, item):
        """
        This method add dates a dictionaty caching
        through key and value.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        This method return the value of the one date or key
        is this date not exist return None through management errors.
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
