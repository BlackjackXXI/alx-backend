#!/usr/bin/env python3
"""baseic cash module
"""


class BaseCaching():
    """baseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    """
    MAX_ITEMS = 4

    def __init__(self):
        """inittttttttttttttttt
        """
        self.cache_data = {}

    def print_cache(self):
        """pinting the resdsss
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """adding gggggggggggggg
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """fetchhhhhhhhhhhhhhhhhh
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
