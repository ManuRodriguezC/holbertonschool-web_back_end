#!/usr/bin/env python3
"""MRU caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    This class acts as the algorithm MRU
    More recently uses, for can to add a new date, this need
    delete a more recently used date.
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
        This method add a new date, with differents condictions
        if teh size is lager tha the size allowed, this method need
        found where value is more recently used and delele this and
        ad a new value.
        """
        size = len(self.cache_data)
        size_max = self.MAX_ITEMS
        if key is not None and item is not None:
            if size < size_max:
                self.last_use = key
                self.cache_data[key] = item
            else:
                print(f"DISCARD: {self.last_use}")
                if key not in self.cache_data:
                    self.cache_data.pop(self.last_use)
                self.cache_data[key] = item
                self.last_use = key

    def get(self, key):
        """
        This method return a specific value in the
        caching collection, if not exist,
        return None.
        """
        try:
            if key in self.cache_data:
                self.last_use = key
            return self.cache_data[key]
        except KeyError:
            return None
