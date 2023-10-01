#!/usr/bin/env python3
""""""

def index_range(page, page_size):
    """"""
    index = page - 1
    start_index = index * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
