#!/usr/bin/env python3
"""FIFO chache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class inherits from BaseCaching and search add dates
    in the dictionary with some condiccions.
    This class try to implement FIFO algori
    """

    def __init__(self):
        """This method overload all attributs and methos of the parent"""
        super().__init__()

    def put(self, key, item):
        """
        This method add dates at dictionary,
        but this method try to will be how FIFO algorhimt
        When the size is larger that allowed this need to delete.
        The fist value add is the fist value delete
        First in First Out(FIFO)
        """
        size = len(self.cache_data)
        max_size = self.MAX_ITEMS
        if key is not None and item is not None:
            if size >= max_size and key not in self.cache_data:
                for k in self.cache_data.keys():
                    print(f"DISCARD: {k}")
                    firt_key = k
                    break
                self.cache_data.pop(firt_key)
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
