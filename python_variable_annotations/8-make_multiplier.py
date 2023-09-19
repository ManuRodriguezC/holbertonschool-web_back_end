#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This funcion receives a float
    Retrun a the function that return the number at square
    """
    def mul(num: float) -> float:
        return num * multiplier
    return mul
