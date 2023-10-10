#!/usr/bin/env python3

"""
Module: 0-basic_async_syntax

This module provides utility functions for asynchronous operations.
"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (inclusive) seconds.

    Args:
        max_delay (float, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The randomly generated delay.

    Example:
        result = await wait_random()
        print("Random delay:", result)
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
