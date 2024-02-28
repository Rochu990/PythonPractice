import unittest
from converters import from_binary_to_decimal_converter, from_decimal_to_binary_converter


class TestTtansmiters(unittest.TestCase):
    def test_from_binary_to_decimal_converter(self):
        self.assertEqual(from_binary_to_decimal_converter(0), 0)
        self.assertEqual(from_binary_to_decimal_converter(1), 1)
        self.assertEqual(from_binary_to_decimal_converter(1010), 10)
        self.assertEqual(from_binary_to_decimal_converter(110110), 54)

    def test_from_decimal_to_binary_converter(self):
        self.assertEqual(from_decimal_to_binary_converter(0), 0)
    def test_from_decimal_to_binary_converter2(self):
        self.assertEqual(from_decimal_to_binary_converter(1), 1)
    def test_from_decimal_to_binary_converter3(self):
        self.assertEqual(from_decimal_to_binary_converter(10), 1010)
        self.assertEqual(from_decimal_to_binary_converter(54), 110110)
        
        


if __name__ == '__main__':
    unittest.main()
        