#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function receives a list of ints and float
    Return the sum of the all values
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
