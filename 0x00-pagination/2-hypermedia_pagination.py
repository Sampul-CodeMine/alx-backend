#!/usr/bin/env python3
"""
This is a module that performs Simple Helper functionality for Pagination
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This is a function that retrieves the index range from a page

    Args:
        page (int) - the page to get its index
        page_size (int) - the size of the page

    Returns:
        Tuple[int, int] - A tuple of integer values
    """
    begin = (page - 1) * page_size
    stop = begin + page_size
    return (begin, stop)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This is a method that retrieves a data page:
        Args:
            page (int) the page with a default value of 1
            page_size (int) the page size with default value pf 10
        Returns:
            List of List - List[List]
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        begin, stop = index_range(page, page_size)
        try:
            data = self.dataset()
            return data[begin:stop]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        This is a method that retrieves information about a page
        Args:
            page (int) the page with a default value of 1
            page_size (int) the page size with default value pf 10
        Returns:
            Dictionary of key:value pairs
        """
        data = self.get_page(page, page_size)
        begin, stop = index_range(page, page_size)
        pages_count = math.ceil(len(self.__dataset) / page_size)
        info_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if stop < len(self.__dataset) else None,
            'prev_page': page - 1 if begin > 0 else None,
            'total_pages': pages_count
        }
        return info_dict
