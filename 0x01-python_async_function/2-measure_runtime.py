#!/usr/bin/env python3
"""
Module: 2-measure_runtime

This module provides a function to measure the runtime of the wait_n
function from the basic_async_syntax module.
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per iteration.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds for each wait_n call.

    Returns:
        float: The average time per iteration, in seconds.

    Example:
        average_time = measure_time(5, 10)
        print("Average time:", average_time)
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start_time
    average_time: float = total_time / n
    return average_time
