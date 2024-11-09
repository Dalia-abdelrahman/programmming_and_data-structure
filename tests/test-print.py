#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from print import say_my_name

class NameDisplayTests(unittest.TestCase):
    def setUp(self):
        """Prepare test environment"""
        self.output_capture = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.output_capture

    def tearDown(self):
        """Restore test environment"""
        sys.stdout = self.original_stdout
        self.output_capture.close()

    def validate_output(self, expected_output):
        """Helper to validate captured output"""
        self.assertEqual(self.output_capture.getvalue(), expected_output)

    def test_name_variants(self):
        """Test various valid name combinations"""
        test_cases = [
            {
                'inputs': ('Alexander', 'Graham'),
                'expected': 'My name is Alexander Graham\n'
            },
            {
                'inputs': ('Marie',),
                'expected': 'My name is Marie \n'
            },
            {
                'inputs': ('Leonardo', 'da Vinci'),
                'expected': 'My name is Leonardo da Vinci\n'
            }
        ]

        for case in test_cases:
            with self.subTest(inputs=case['inputs']):
                self.output_capture.seek(0)
                self.output_capture.truncate()
                say_my_name(*case['inputs'])
                self.validate_output(case['expected'])

    def test_invalid_inputs(self):
        """Test various invalid input combinations"""
        invalid_cases = [
            {'primary': 123, 'secondary': 'Smith'},
            {'primary': None, 'secondary': 'Smith'},
            {'primary': 'John', 'secondary': 123},
            {'primary': [], 'secondary': 'Smith'},
            {'primary': 'John', 'secondary': None}
        ]

        for case in invalid_cases:
            with self.subTest(case=case):
                with self.assertRaises(TypeError):
                    say_my_name(case['primary'], case['secondary'])

if __name__ == '__main__':
    unittest.main()
