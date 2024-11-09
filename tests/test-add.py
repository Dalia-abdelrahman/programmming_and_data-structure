#!/usr/bin/python3
import unittest
from add import add_integer

class AdditionOperationTests(unittest.TestCase):
    def setUp(self):
        """Initialize test cases"""
        self.valid_test_sets = [
            {"inputs": (10, 20), "expected": 30},
            {"inputs": (-30, 10), "expected": -20},
            {"inputs": (2.5, 3.5), "expected": 5},
            {"inputs": (100.9, -2.1), "expected": 98},
            {"inputs": (5,), "expected": 103},
        ]
        
        self.invalid_test_sets = [
            {"input": ("str", 20), "error_type": TypeError},
            {"input": (10, "str"), "error_type": TypeError},
            {"input": (None, 20), "error_type": TypeError},
            {"input": ({}, []), "error_type": TypeError},
        ]

    def test_valid_operations(self):
        """Test all valid addition scenarios"""
        for test_set in self.valid_test_sets:
            with self.subTest(msg=f"Testing {test_set}"):
                result = add_integer(*test_set["inputs"])
                self.assertEqual(result, test_set["expected"])

    def test_invalid_operations(self):
        """Test all invalid addition scenarios"""
        for test_set in self.invalid_test_sets:
            with self.subTest(msg=f"Testing {test_set}"):
                with self.assertRaises(test_set["error_type"]):
                    add_integer(*test_set["input"])

if __name__ == '__main__':
    unittest.main()
