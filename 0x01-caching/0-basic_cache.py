#!/usr/bin/env python3
"""caching
"""
from base_caching import BaseCaching
class BasicCache(BaseCaching):
    """12345
    """
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item
    def get(self, key):
        return self.cache_data.get(key, None)
