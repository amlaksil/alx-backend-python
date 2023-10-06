#!/usr/bin/env python3
"""
9-element_length
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples containing elements from the input list
    and their corresponding lengths.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing elements from
        the input list and their lengths.

    Example:
        >>> element_length(['apple', 'banana', 'cherry'])
        [('apple', 5), ('banana', 6), ('cherry', 6)]
    """
    return [(i, len(i)) for i in lst]
