#!/usr/bin/env python3
"""
This module provides a function for zooming in on an array by repeating each
element by a specified factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the given array by repeating each element by the
    specified factor.

    Args:
        lst (Tuple): The input array to be zoomed in.
        factor (int): The factor by which each element
        should be repeated. Defaults to 2.

    Returns:
        List: The zoomed-in array.

    Example:
        >>> array = (12, 72, 91)
        >>> zoom_2x = zoom_array(array)
        >>> print(zoom_2x)
        [12, 12, 72, 72, 91, 91]

        >>> zoom_3x = zoom_array(array, 3)
        >>> print(zoom_3x)
        [12, 12, 12, 72, 72, 72, 91, 91, 91]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Use tuple instead of list for array

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Remove decimal point from factor value
