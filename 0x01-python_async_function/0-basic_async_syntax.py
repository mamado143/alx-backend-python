#!usr/bin/env python3
'''Task async function.
'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
