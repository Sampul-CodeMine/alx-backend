#!/usr/bin/env python3
"""
This is a module that performs Simple Helper functionality for Pagination
"""
from typing import Tuple


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
