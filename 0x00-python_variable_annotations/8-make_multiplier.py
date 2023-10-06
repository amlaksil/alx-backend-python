#!/usr/bin/env python3
"""
8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a float by
        the multiplier.
    Example:
        >>> doubler = make_multiplier(2.0)
        >>> doubler(3.5)
        7.0
    """
    return lambda n: n * multiplier
