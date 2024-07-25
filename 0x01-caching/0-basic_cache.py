#!/usr/bin/env python3
"""aertg
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """satrhe
    """
    def put(self, key, item):
        """aswtrh
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """treh
        """
        return self.cache_data.get(key, None)
