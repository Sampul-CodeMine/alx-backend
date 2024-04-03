#!/usr/bin/env python3
"""
Module implements Basic Caching using MRU (Most Recently Used) Cache Logic
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This is a class that defines MFUCache inheriting from BaseCache"""
    def __init__(self):
        """Class Constructor"""
        super().__init__()
        self.buff_mem = []

    def put(self, key, item):
        """
        This is a method that allows adding of key value pair to the cache
        Args:
            key - the key of the data to be added
            item - the value of the data to be added
        """
        if key is not None or item is not None:
            if self.cache_data.get(key):
                self.buff_mem.remove(key)
            while len(self.buff_mem) >= self.MAX_ITEMS:
                del_key = self.buff_mem.pop()
                self.cache_data.pop(del_key)
                print(f"DISCARD: {del_key}")
            self.buff_mem.append(key)
            self.cache_data[key] = item
        return

    def get(self, key):
        """
        This is a method that retrieves an item from the cache by the key.
        Args:
            key - key to the data to be retrieved.
        """
        if self.cache_data.get(key):
            self.buff_mem.remove(key)
            self.buff_mem.append(key)
        return self.cache_data.get(key, None)
