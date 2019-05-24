"""A3. Tester for the function common_words in tweets.
"""

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    """Tester for the function common_words in tweets.
    """

    def test_empty(self):
        """Empty dictionary."""

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_word_smaller_than_limit(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 2
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_different_freq_1(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 1}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_different_freq_2(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 1}
        arg2 = 2
        exp_arg1 = {'hello': 2, 'h': 1}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_same_freq_1(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_same_freq_2(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2}
        arg2 = 2
        exp_arg1 = {'hello': 2, 'h': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_same_freq_3(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2, 'e': 2}
        arg2 = 2
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_same_freq_4(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2, 'e': 2}
        arg2 = 5
        exp_arg1 = {'hello': 2, 'h': 2, 'e': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_diff_same_freq_1(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2, 'e': 4, 'l': 10}
        arg2 = 1
        exp_arg1 = {'l': 10}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_diff_same_freq_2(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2, 'e': 4, 'l': 10}
        arg2 = 2
        exp_arg1 = {'l': 10, 'e': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_diff_same_freq_3(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2, 'e': 4, 'l': 10}
        arg2 = 3
        exp_arg1 = {'l': 10, 'e': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_multi_words_diff_same_freq_3(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2, 'h': 2, 'e': 4, 'l': 10}
        arg2 = 4
        exp_arg1 = {'l': 10, 'e': 4, 'hello': 2, 'h': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
if __name__ == '__main__':
    unittest.main(exit=False)
