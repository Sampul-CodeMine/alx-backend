#!/usr/bin/env python3
"""
Module implements Basic Caching using LRU (Least Recently Used) Cache Logic
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This is a class that defines LFUCache inheriting from BaseCache"""
    def __init__(self):
        """Class Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        This is a method that allows adding of key value pair to the cache
        Args:
            key - the key of the data to be added
            item - the value of the data to be added
        """
        if key is not None or item is not None:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete_key = self.queue.pop(0)
                self.cache_data.pop(delete_key)
                print(f"DISCARD: {delete_key}")
        return

    def get(self, key):
        """
        This is a method that retrieves an item from the cache by the key.
        Args:
            key - key to the data to be retrieved.
        """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key, None)
