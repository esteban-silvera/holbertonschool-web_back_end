#!/usr/bin/env python3
"""coments"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """cometn"""
    return (k, v ** 2.0)
