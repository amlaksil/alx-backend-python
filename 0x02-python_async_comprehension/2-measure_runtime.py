#!/usr/bin/env python3
"""
Module: 2-measure_runtime

This module provides a coroutine for measuring the runtime of executing
async_comprehension four times in parallel.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: The total runtime in seconds.

    Usage:
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime} seconds")
    """
    start_time: float = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time: float = time.time()
    total_runtime: float = end_time - start_time
    return total_runtime
