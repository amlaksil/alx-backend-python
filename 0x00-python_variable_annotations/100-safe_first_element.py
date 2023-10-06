#!/usr/bin/env python3
"""
Module: 100-safe_first_element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element from a list.

    Args:
        lst: A list or sequence of elements.

    Returns:
        The first element from the list if it exists, or None
        if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
