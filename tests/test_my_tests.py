import unittest

from fundamentals import check_number

class MyTestCases(unittest.TestCase):
    def test_check_number_odd_number(self):
        self.assertEqual(check_number(5), "Weird")

    def test_check_number_even_number(self):
        self.assertEqual(check_number(4), "Not Weird")
        self.assertEqual(check_number(8), "Weird")
        self.assertEqual(check_number(-2), "Very weird")

    def test_check_number_negative_even_number(self):
        self.assertEqual(check_number(-4), "Very weird")
        self.assertEqual(check_number(-6), "Very weird")

    def test_check_number_negative_odd_number(self):
        self.assertEqual(check_number(-3), "Extremely Weird")
        self.assertEqual(check_number(-1), "Extremely Weird")

    def test_check_number_neutral(self):
        self.assertEqual(check_number(0), "Neutral")

if __name__ == '__main__':
    unittest.main()