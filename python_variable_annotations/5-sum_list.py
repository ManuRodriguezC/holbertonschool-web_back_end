#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function receives a list of floats
    Return the sum of the floats in the list
    """
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
