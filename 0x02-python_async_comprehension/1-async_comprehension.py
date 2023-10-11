#!/usr/bin/env python3
"""
Module: 1-async_comprehension

This module provides an asynchronous comprehension coroutine.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers.

    Usage:
        numbers = await async_comprehension()
        print(numbers)
    """
    numbers = [number async for number in async_generator()]
    return numbers
