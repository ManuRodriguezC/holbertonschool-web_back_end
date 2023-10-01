#!/user/bin/env python3
""""""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """"""

    def __inti__(self):
        """"""
        super().__init__()
        self.last_use = None

    def put(self, key, item):
        """"""
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
        """"""
        try:
            if key in self.cache_data:
                self.last_use = key
            return self.cache_data[key]
        except KeyError:
            return None
