#!/usr/bin/env python3
"""
Module:
"""
from typing import TypeVar, Mapping, Any, Optional, Union

K = TypeVar('K')
V = TypeVar('V')


def safely_get_value(dct: Mapping[K, V], key: K, default: Optional[V] = None)-> Union[V, Optional[V]]:
    """
    Safely retrieves a value from a dictionary based on the given key.

    If the key exists in the dictionary, the corresponding value is returned.
    If the key does not exist, the default value is returned.

    Args:
        dct (Mapping[K, V]): The dictionary-like object to retrieve the
        value from.
        key (K): The key to look up in the dictionary.
        default (Optional[V], optional): The default value to return
        if the key does not exist. Defaults to None.

    Returns:
        Union[V, Optional[V]]: The value corresponding to the key
        if it exists in the dictionary, or the default value if provided.
    """
    if key in dct:
        return dct[key]
    else:
        return default
