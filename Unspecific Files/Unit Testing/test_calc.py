########################################################################################
# test_calc.py
#
# Program to demonstrate how to format unit tests.
########################################################################################

import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_integer_division(self):
        self.assertEqual(calc.integer_division(5, 10), 0)
        self.assertEqual(calc.integer_division(4, 1), 4)
        self.assertEqual(calc.integer_division(8, 3), 2)
        self.assertEqual(calc.integer_division(7, 2), 3)
        self.assertEqual(calc.integer_division(0, 3), 0)

        with self.assertRaises(ValueError):
            calc.integer_division(10, 0)

    def test_modulus(self):
        self.assertEqual(calc.modulus(5, 10), 5)
        self.assertEqual(calc.modulus(4, 1), 0)
        self.assertEqual(calc.modulus(8, 3), 2)
        self.assertEqual(calc.modulus(7, 2), 1)
        self.assertEqual(calc.modulus(0, 3), 0)

        with self.assertRaises(ValueError):
            calc.integer_division(10, 0)

    def test_exponentiation(self):
        self.assertEqual(calc.exponentiation(5, 10), 9765625)
        self.assertEqual(calc.exponentiation(4, 1), 4)
        self.assertEqual(calc.exponentiation(8, 3), 512)
        self.assertEqual(calc.exponentiation(7, 2), 49)
        self.assertEqual(calc.exponentiation(0, 3), 0)
        self.assertEqual(calc.exponentiation(3, 0), 1)
        self.assertEqual(calc.exponentiation(-2, 3), -8)
        self.assertEqual(calc.exponentiation(-2, 4), 16)


# if statement allows unit test to run if file ran directly
# otherwise would need to use `python -m unittest test_calc.py`
if __name__ == "__main__":
    unittest.main()