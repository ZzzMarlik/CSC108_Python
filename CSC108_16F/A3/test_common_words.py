import unittest
import tweets


class TestCommonWords(unittest.TestCase):

    def test_none_removed(self):
        """ Test common_words with N so that no words are removed. """

        words_to_counts = {'cat': 1}
        expected_result = {'cat': 1}
        tweets.common_words(words_to_counts, 1)
        self.assertEqual(words_to_counts, expected_result, 'none removed')

    # Place your unit test definitions after this line.
    def test_empty_dictionary(self):
        """ Test common_words with empty dictionary. """
        words_to_counts = {}
        expected_result = {}
        tweets.common_words(words_to_counts, 1)
        self.assertEqual(words_to_counts, expected_result, {})

    def test_normal_dictionary(self):
        """ Test common_words with normal dictionary. """
        words_to_counts = {'Mark': 10, 'Eve': 12, 'Tiffany': 9}
        expected_result = {'Eve': 12}
        tweets.common_words(words_to_counts, 1)
        self.assertEqual(words_to_counts, expected_result, {'Eve': 12})
        
    def test_dictionary_with_Tie(self):
        """ Test common_words with Tie values. """
        words_to_counts = {'Mark': 13, 'Eve': 12, 'Tiffany': 12}
        expected_result = {'Mark': 13}
        tweets.common_words(words_to_counts, 2)
        self.assertEqual(words_to_counts, expected_result, {'Mark': 13})

    def test_dictionary_with_Tie2(self):
        """ Test common_words with Tie values but different N. """
        words_to_counts = {'Mark': 13, 'Eve': 12, 'Tiffany': 12}
        expected_result = {'Mark': 13, 'Eve': 12, 'Tiffany': 12}
        tweets.common_words(words_to_counts, 3)
        self.assertEqual(words_to_counts, expected_result, {'Mark': 13, 'Eve': 12, 'Tiffany': 12}) 

# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
