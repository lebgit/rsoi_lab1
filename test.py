import unittest
from functions import prime_num, square


prime_test_data = ['1', '2', '3', '4', '5', '6', '7']
prime_test_result = [True, True, True, False, True, False, True]

square_test_data = ['1', '2', '3', '4', '5', '6', '7']
square_test_result = [1, 4, 9, 16, 25, 36, 49]


class TestNum(unittest.TestCase):

    def test_prime(self):
        for i, item in enumerate(prime_test_data):
            with self.subTest(text="sequence: "+item):
                self.assertEqual(prime_num(item), prime_test_result[i])

    def test_square(self):
        for i, item in enumerate(square_test_data):
            with self.subTest(text="sequence: "+item):
                self.assertEqual(square(item), square_test_result[i])

if __name__ == '__main__':
    unittest.main()
