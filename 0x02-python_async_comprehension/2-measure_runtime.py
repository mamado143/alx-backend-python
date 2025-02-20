#!/usr/bin/env python3
'''Task2 solution.
'''
import asyncio
import time
from importlib import import_module as im

async_comprehension = im('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times,
    and measures the
    total execution time.

    Returns:
        The total execution time in seconds as a float.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
