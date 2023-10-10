#!/usr/bin/env python3
"""
Module: 3-tasks

This module provides a function to create an asyncio task that executes
the wait_random coroutine.
"""
import asyncio
from typing import Coroutine
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio task that executes the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for the wait_random
        coroutine.

    Returns:
        asyncio.Task: A task representing the execution of the wait_random
        coroutine.

    Example:
        task = task_wait_random(5)
        await task
        result = task.result()
        print(result)
    """
    task: asyncio.Task[float] = asyncio.create_task(wait_random(max_delay))
    return task
