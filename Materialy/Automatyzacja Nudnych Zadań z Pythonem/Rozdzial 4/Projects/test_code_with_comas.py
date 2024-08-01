import unittest

from code_with_comas import code_with_comas


class TestCodeWithComas(unittest.TestCase):
    def test_empty_list(self):
        words = []
        self.assertEqual(code_with_comas(words), "")

    def test_list_with_one_word(self):
        words = ["word1"]
        self.assertEqual(code_with_comas(words), "word1")

    def test_list_with_two_words(self):
        words = ["word1", "word2"]
        self.assertEqual(code_with_comas(words), "word1 i word2")

    def test_list_with_more_than_two_words(self):
        words = ["word1", "word2", "word3", "word4"]
        self.assertEqual(code_with_comas(words), "word1, word2, word3 i word4")


if __name__ == "__main__":
    unittest.main()
