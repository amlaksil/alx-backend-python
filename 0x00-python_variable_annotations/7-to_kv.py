#!/usr/bin/env python3
"""
Module: 7-to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k and the square of int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the
        square of v as a float.

    Example:
        >>> to_kv("length", 5)
        ('length', 25.0)
        >>> to_kv("pi", 3.14159)
        ('pi', 9.8695877281)
    """
    return k, float(v ** 2)
