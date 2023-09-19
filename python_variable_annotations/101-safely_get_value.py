#!/usr/bin/env python3
"""This module create and note the annotations variables"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'),
                                    None] = None)-> Union[Any,
                                                          TypeVar('T')]:
    """
        This function receives three params:
        dct: This is a mapping type, can be tu loop the value
        Key: This is a any date, must be an int
        defaul: This a type if the one class or T class or nothing
        Retrun the ant date, can be  int o a T
    """
    if key in dct:
        return dct[key]
    else:
        return default
