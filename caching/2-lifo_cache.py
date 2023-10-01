#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    This class acts as the algorithm LIFO
    Last in First out, this add dates of the diccionary when
    the size is less that the max size, if teh size is larger
    the key and value replace the last value add in the dictionary
    """

    def __init__(self):
        """
        This method init the class lifo
        and add a new value, when the value exist in the
        dictionary and change, this value save for change in the next
        put or add new value in it.
        """
        super().__init__()
        self.key_change = None

    def put(self, key, item):
        """
        This methos add a new value in the dictionary
        if the value exist before, this change nad save the key
        for the nex change, this value replace por the new
        """
        size = len(self.cache_data)
        max_size = self.MAX_ITEMS
        if key is not None and item is not None:
            if size >= max_size:
                last = next(reversed(list(self.cache_data)))
                if key in self.cache_data:
                    self.key_change = key
                    self.cache_data[key] = item
                if self.key_change is not None:
                    self.cache_data.pop(self.key_change)
                    self.cache_data[key] = item
                    self.key_change = None
                else:
                    self.cache_data.pop(last)
                    self.cache_data[key] = item
                    print(f"DISCARD: {last}")
            if key not in self.cache_data:
                self.cache_data[key] = item
            else:
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
