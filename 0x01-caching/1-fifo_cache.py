#!/usr/bin/env python3
"""zDFB
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """zfdbn
    """
    def __init__(self):
        """zDFBN
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """zDFB
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """dfbtafrg.
        """
        return self.cache_data.get(key, None)
