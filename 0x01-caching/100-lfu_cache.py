#!/usr/bin/env python3
"""
Module implements Basic Caching using LFU (Least Frequently Used) Cache Logic
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This is a class that defines MFUCache inheriting from BaseCache"""
    def __init__(self):
        """Class Constructor"""
        super().__init__()
        self.bfm = []
        self.lfu = {}

    def put(self, key, item):
        """
        This is a method that allows adding of key value pair to the cache
        Args:
            key - the key of the data to be added
            item - the value of the data to be added
        """
        if key is not None or item is not None:
            if len(self.bfm) >= self.MAX_ITEMS and \
                    not self.cache_data.get(key):
                del_key = self.bfm.pop(0)
                self.lfu.pop(del_key)
                self.cache_data.pop(del_key)
                print(f"DISCARD: {del_key}")
            if self.cache_data.get(key):
                self.bfm.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            idx = 0
            while idx < len(self.bfm) and not self.lfu[self.bfm[idx]]:
                idx += 1
            self.bfm.insert(idx, key)
            self.cache_data[key] = item

        return

    def get(self, key):
        """
        This is a method that retrieves an item from the cache by the key.
        Args:
            key - key to the data to be retrieved.
        """
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.bfm.index(key) + 1 != len(self.bfm):
                while(self.bfm.index(key) + 1 < len(self.bfm)
                      and self.lfu[key] >=
                      self.lfu[self.bfm[self.bfm.index(key) + 1]]):
                    self.bfm.insert(self.bfm.index(key) + 1,
                                    self.bfm.pop(self.bfm.index(key)))
        return self.cache_data.get(key, None)
