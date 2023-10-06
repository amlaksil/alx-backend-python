#!/usr/bin/env python3
"""
Module: 5-sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of input_list numbers.
    Args:
        input_list (List[float]): A list of float number.
    """
    sum: float = 0.0
    for n in input_list:
        sum += n
    return sum
