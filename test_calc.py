import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_divide(self):
        # self.assertRaises(ValueError, calc.divided, 10, 0)
        with self.assertRaises(ValueError):
            calc.divided(10, 0)


if __name__ == '__main__':
    unittest.main()