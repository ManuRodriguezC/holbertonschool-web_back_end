#!/usr7bin/env python3
"""LRU cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """"""

    def __init__(self):
        super().__init__()
        self.list_uses = {}

    def put(self, key, item):
        """"""
        size = len(self.cache_data)
        size_list = len(self.list_uses)
        max_size = self.MAX_ITEMS
        size_save = self.MAX_ITEMS - 1
        if key is not None and item is not None:
            if size < max_size:
                self.cache_data[key] = item
                if size_list >= size_save:
                    for i in self.list_uses.keys():
                        first = i
                        break
                    self.list_uses.pop(first)
                    self.list_uses[key] = item
                else:
                    self.list_uses[key] = item
            else:
                if key not in self.cache_data:
                    for k in self.cache_data.keys():
                        if k not in self.list_uses:
                            clean = k
                    for k in self.list_uses.keys():
                        first_list = k
                        break
                    self.list_uses.pop(first_list)
                    self.list_uses[key] = item
                    self.cache_data.pop(clean)
                    print(f"DISCARD: {clean}")
                    self.cache_data[key] = item

                else:
                    self.cache_data[key] = item
                    for i in self.list_uses.keys():
                        f = i
                        break
                    self.list_uses.pop(f)
                    self.list_uses[key] = item

    def get(self, key):
        """"""
        try:
            if key in self.list_uses:
                value = self.list_uses[key]
                self.list_uses.pop(key)
                self.list_uses[key] = value
                return self.cache_data[key]
            else:
                for i in self.list_uses.keys():
                    first = i
                    break
                item = self.list_uses[key]
                self.list_uses.pop(first)
                self.list_uses[key] = item
                return self.cache_data[key]
        except KeyError:
            return None
