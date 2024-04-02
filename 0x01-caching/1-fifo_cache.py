#!/usr/bin/env python3
"""
Module to implement Basic Caching using FIFO (First In First Out) Queue Logic
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    This is a class that inherits from the BaseCaching parent class
    It implements FIFO Queue system for caching
    """
    def __init__(self):
        """Constructor of FIFOCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        This is a method that allows adding of key value pair to the cache
        Args:
            key - the key of the data to be added
            item - the value of the data to be added
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_data_key, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {first_data_key}")

        return

    def get(self, key):
        """
        This is a method that retrieves an item from the cache by the key.
        Args:
            key - key to the data to be retrieved.
        """
        return self.cache_data.get(key, None)
