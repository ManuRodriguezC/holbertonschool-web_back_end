#!/usr/bin/env python3
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple:
    return (k, float(v ** 2))