#!/usr/bin/env python3
"""coments"""


import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """coment"""
    delays = [wait_random(max_delay) for x in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
