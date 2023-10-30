#!/usr/bin/env python3

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised when accessing a non-existent
        key in the nested map.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result.

        Args:
                test_url (str): The test URL.
                test_payload (dict): The expected payload returned by get_json.
                mock_get (Mock): The mocked requests.get function.

        Returns:
                None

        Raises:
                AssertionError: If the mocked get method is not called exactly
                once with test_url as argument.
                If the output of get_json is not equal to test_payload.
        """
        with patch('requests.get') as mock_get:
            # Configure the mock get method
            mock_response = mock_get.return_value
            mock_response.json.return_value = test_payload

            # Call the get_json function
            result = get_json(test_url)

            # Assert that the mocked get method is called exactly once
            # with test_url as argument
            mock_get.assert_called_once_with(test_url)

            # Assert that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for memoize function."""

    def test_memoize(self):
        """
        Test the memoize decorator.

        This method creates an instance of TestClass and tests the behavior
        of the memoize decorator. It patches the a_method of TestClass with
        a mock object and verifies that the a_method is called only once. It
        also checks that the results of the memoized property are equal.
        """
        class TestClass:
            """Class for testing the memoize decorator."""

            def a_method(self):
                """Method to be memoized."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property."""
                return self.a_method()
        # Create an instance of TestClass
        test_object = TestClass()

        # Patch the a_method of TestClass
        with patch.object(TestClass, 'a_method') as mock_a_method:
            # Configure the mock object
            mock_a_method.return_value = 42

            # Call the a_property twice
            result1 = test_object.a_property
            result2 = test_object.a_property

            # Assert that a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that the results are equal
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
