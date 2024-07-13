"""""import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        result = 2 + 3
        self.assertEqual(result, 5)

    def test_add_one_negative_number(self):
        result = 10 + -4
        self.assertEqual(result, 6)
    
    def test_add_two_negative_numbers(self):
        result = -8 + -3
        self.assertEqual(result, -11)

    def test_subtract(self):
        result = 10 - 2
        self.assertEqual(result, 8)
    
    def subtract_one_negative_number(self):
        result = 10 - -3
        self.assertEqual(result, 7)

    def test_subtract_two_negative_numbers(self):
        result = -10 - 3
        self.assertEqual(result, -13)

    def test_multiply(self):
        result = 2 * 4
        self.assertEqual(result, 8)
    
    def test_multiply_one_negative_number(self):
        result = 2 * -4
        self.assertEqual(result, -8)

    def test_divide(self):
        result = 8 / 2
        self.assertEqual(result, 4)

    def test_divide_one_negative_number(self):
        result = -10 / 5
        self.assertEqual(result, -2)

    def test_divided_by_zero(self):
        try:
            result = 1 / 0
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        

if __name__ == "__main__":
    unittest.main() """""""""""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-8, 4), -12)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-4, 4), -16)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        try:
            self.assertEqual(self.calc.divide(1, 0), )
        except ZeroDivisionError as e:
            print(f"Error {e}")
        except TypeError as e:
            print(f"{e} is not of the correct type")

if __name__ == "__main__":
    unittest.main()

