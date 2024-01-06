#!/usr/bin/env python3
"""coments"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """coment"""
    return [(i, len(i)) for i in lst]