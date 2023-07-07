import unittest

from zadanie_4 import fun

words = ['ala', 'ola']

class TestCalc(unittest.TestCase):
    def test_fun(self):
        result = fun(words)
        self.assertEqual(['ala 3', 'ola 3'], result)

if __name__ == '__main__':
    unittest.main()