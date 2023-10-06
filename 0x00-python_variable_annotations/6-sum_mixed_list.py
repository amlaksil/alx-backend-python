#!/usr/bin/python3
"""
Module: 6-sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of integers and floats in a mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the numbers in the mixed list.

    Example:
        >>> sum_mixed_list([1, 2.5, 3, 4.7])
        11.2
    """
    return float(sum(mxd_lst))
