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
