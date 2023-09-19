#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This funcion receives a list that can be iterable
    Return a new list with the tuble values
    """
    return [(i, len(i)) for i in lst]
