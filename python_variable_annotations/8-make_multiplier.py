#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mul(num: float) -> float:
        return num * multiplier
    return mul  