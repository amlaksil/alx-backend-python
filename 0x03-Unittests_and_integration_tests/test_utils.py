#!/usr/bin/env python3

from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with different inputs.

        Args:
        ----------
        nested_map : Mapping
            A nested map.
        path : Sequence
            A sequence of keys representing the path to the value.
        expected_result : Any
            The expected result when accessing the nested map with
            the given path.

        Returns
        -------
        None

        Raises
        ------
        AssertionError
            If the result of accessing the nested map does
            not match the expected result.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
