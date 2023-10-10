#!/usr/bin/env python3
"""
Module: 1-concurrent_coroutines

This module provides utility functions for asynchronous operations.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns wait_random n times with the specified
    max_delay. It returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random coroutine.
        max_delay (int): The maximum delay in seconds for each wait_random
        coroutine.

    Returns:
        List[float]: The list of delays (float values) in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
