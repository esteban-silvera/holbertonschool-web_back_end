#!/usr/bin/env python3
"""coments"""
import asyncio


from . import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """coments"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
