#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function receives a lst that is a secencie for any type
    Return the union of anytypes or nothing
    """
    if lst:
        return lst[0]
    else:
        return None
    