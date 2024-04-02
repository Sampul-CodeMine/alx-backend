#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This is a method that implements a hyper index on pagination
        Args:
            index (int) with default value of None
            page_size (int) with default value of 10
        Returns:
            Dictionary (key:value) pairs
        """
        data = self.indexed_dataset()
        assert index >= 0 and index <= max(data.keys())
        page_index = {}

        count = index

        while len(page_index) < page_size and count < len(self.dataset()):
            if count in data:
                page_index[count] = data[count]
            count += 1

        page = list(page_index.values())
        page_log = page_index.keys()
        return {
            'index': index,
            'next_index': max(page_log) + 1,
            'page_size': len(page),
            'data': page
        }
