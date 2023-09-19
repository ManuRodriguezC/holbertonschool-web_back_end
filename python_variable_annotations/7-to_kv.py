#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This funcion receives two arguments
    k: Is a string
    v: Is a number which can be int or float
    Return the string a the num at square
    """
    return (k, float(v ** 2))
