#!/usr/bin/env python3
""""""
import csv
import math
from typing import List
import os



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
        # Check if the page and page size are integers
        assert isinstance(page, int), "page must be an integer"
        assert isinstance(page_size, int), "page_size must be an integer"
        assert page > 0, "page must be greater than 0"
        assert page_size > 0, "page_size must be greater than 0"

        # Use the index_range function to get the start and end index
        start_index, end_index = index_range(page, page_size)

        # Use the len function to get the length of the dataset
        dataset_length = len(self.dataset())

        # If the end index is greater than the dataset length, set it to the dataset length
        if end_index > dataset_length:
            end_index = dataset_length

        # Use slicing to get the page of data from the dataset
        page_data = self.dataset()[start_index:end_index]

        # Return the page of data
        return page_data


def index_range(page, page_size):
    """"""
    index = page - 1
    start_index = index * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
