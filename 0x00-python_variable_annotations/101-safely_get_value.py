#!/usr/bin/env python3
"""
This module provides a function for safely retrieving values from a dictionary.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key whose value needs to be retrieved.
        default (Union[T, None], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key if it exists in
        the dictionary, otherwise the default value.

    Example:
    >>> dct = {'a': 1, 'b': 2, 'c': 3}
    >>> safely_get_value(dct, 'a')
    1
    >>> safely_get_value(dct, 'd', default='Not found')
    'Not found'
    """
    if key in dct:
        return dct[key]
    else:
        return default
