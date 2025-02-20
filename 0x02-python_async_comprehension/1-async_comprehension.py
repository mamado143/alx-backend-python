#!/usr/bin/env python3
'''Task 1 solution.
'''
from typing import List
from importlib import import_module as im

async_generator = im('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers from async_generator.

    Returns:
        A list of 10 random numbers generated by async_generator.
    '''
    return [num async for num in async_generator()]
