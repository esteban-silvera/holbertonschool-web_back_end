#!/usr/bin/env python3
"""coments"""


import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """coment"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)