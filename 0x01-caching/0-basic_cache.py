#!/usr/bin/env python3
"""
Module to implement Basic Caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This is a class that inherits from the BaseCaching parent class
    It allows for storing and retrieving key-value pairs from a dictionary.
    """
    def put(self, key, item):
        """
        This is a method that allows adding of key value pair to the cache
        Args:
            key - the key of the data to be added
            item - the value of the data to be added
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
        return

    def get(self, key):
        """
        This is a method that retrieves an item from the cache by the key.
        Args:
            key - key to the data to be retrieved.
        """
        return self.cache_data.get(key, None)
