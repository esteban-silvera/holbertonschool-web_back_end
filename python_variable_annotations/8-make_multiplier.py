#!/usr/bin/env python3
"""coments"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """coment"""
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
