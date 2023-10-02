#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """
    This function return the number of elements
    in each page, and return a set with elements in the page
    """
    index = page - 1
    start_index = index * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
