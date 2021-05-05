import unittest

from sample_func import add, subtract, multiply, division


class TestOne(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 9), 13)
        self.assertEqual(add(-3, 9), 6)

    def test_subtract(self):
        self.assertEqual(subtract(4, 9), -5)
        self.assertEqual(subtract(-3, 9), -12)

    def test_multiply(self):
        self.assertEqual(multiply(4, 9), 36)
        self.assertEqual(multiply(-3, 9), -27)

    def test_division(self):
        self.assertEqual(round(division(4, 9)), 0)
        self.assertEqual(division(18, 9), 2)
        self.assertRaises(ZeroDivisionError, division, 4, 0)


if __name__ == '__main__':
    unittest.main()
