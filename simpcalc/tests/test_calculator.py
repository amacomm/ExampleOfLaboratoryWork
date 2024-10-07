'''
Модуль тестирования работы класса простого калькулятора.
'''
import unittest
import numpy as np
from simpcalc.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    # В данном случае тест не верный, почему?
    def test_divide_by_numpy_array_with_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, np.array([1, 2, 0, 5]))


if __name__ == "__main__":
    unittest.main()
