import bodmas
import unittest

class TestBodmas(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(bodmas.addition(3, 1), 4)
        self.assertEqual(bodmas.addition(20, 1), 21)
        self.assertEqual(bodmas.addition(10, -1), 9)

    def test_subtraction(self):
        self.assertEqual(bodmas.subtraction(3, 1), 2)
        self.assertEqual(bodmas.subtraction(20, 1), 19)
        self.assertEqual(bodmas.subtraction(10, -1), 11)

    def test_multiplication(self):
        self.assertEqual(bodmas.multiplication(3, 1), 3)
        self.assertEqual(bodmas.multiplication(20, 1), 20)
        self.assertEqual(bodmas.multiplication(10, -1), -10)

    def test_division(self):
        self.assertEqual(bodmas.division(3, 1), 3)
        self.assertEqual(bodmas.division(20, 1), 20)
        self.assertEqual(bodmas.division(10, -1), -10)

if __name__ == '__main__':
    unittest.main()