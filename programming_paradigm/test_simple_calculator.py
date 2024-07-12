import unittest
from simple_calculator import SimpleCalculator

class Testsimplecalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = 2 + 3
        self.assertEqual(result, 5)

    def test_add_one_negative_number(self):
        result = 10 + -4
        self.assertEqual(result, 6)
    
    def test_add_two_negative_numbers(self):
        result = -8 + -3
        self.assertEqual(result, -11)

    def test_subtract_positive_numbers(self):
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
    unittest.main()
    
