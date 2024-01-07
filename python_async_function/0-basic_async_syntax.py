#!/usr/bin/env python3
"""coments"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """coment"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
