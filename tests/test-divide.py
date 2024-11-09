#!/usr/bin/python3
import unittest
from divide import matrix_divided

class MatrixOperationsTest(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.base_matrix = [
            [2.0, 4.0, 6.0],
            [8.0, 10.0, 12.0]
        ]
        
        self.test_scenarios = {
            'basic': {
                'matrix': [[2, 4, 6], [8, 10, 12]],
                'factor': 2,
                'expected': [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
            },
            'decimals': {
                'matrix': [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]],
                'factor': 1.5,
                'expected': [[1.0, 1.67, 2.33], [3.0, 3.67, 4.33]]
            },
            'negatives': {
                'matrix': [[-2, -4, -6], [-8, -10, -12]],
                'factor': -2,
                'expected': [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
            }
        }

    def test_valid_operations(self):
        """Test various valid matrix division operations"""
        for scenario_name, data in self.test_scenarios.items():
            with self.subTest(scenario=scenario_name):
                result = matrix_divided(data['matrix'], data['factor'])
                self.assertEqual(result, data['expected'])

    def test_invalid_matrices(self):
        """Test invalid matrix inputs"""
        invalid_matrices = [
            None,
            "not a matrix",
            [[1, 2], [3, "4"]],
            [[1], [1, 2]],
            [[1, 2], [3, 4, 5]]
        ]
        for invalid_matrix in invalid_matrices:
            with self.subTest(matrix=invalid_matrix):
                with self.assertRaises(TypeError):
                    matrix_divided(invalid_matrix, 2)

    def test_invalid_factors(self):
        """Test invalid division factors"""
        invalid_factors = [
            0,
            "2",
            None,
            [2],
            {'factor': 2}
        ]
        for invalid_factor in invalid_factors:
            with self.subTest(factor=invalid_factor):
                with self.assertRaises((TypeError, ZeroDivisionError)):
                    matrix_divided(self.base_matrix, invalid_factor)

if __name__ == '__main__':
    unittest.main()
