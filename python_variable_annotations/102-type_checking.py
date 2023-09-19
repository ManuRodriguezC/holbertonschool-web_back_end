#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    This funcion receives two arguments
    lst: The fist is a tuple
    factor: This second is a int
    And return the tuple
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
