"""A3. Tester for the function extract_mentions in tweets.
"""

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    """Tester for the function extract_mentions in tweets.
    """

    def test_empty(self):
        """Empty tweet."""

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        """Non-empty tweet with no mentions."""

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_one_mention_no_tag(self):
        arg = 'tweet @test case'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_one_tag_no_mention(self):
        arg = 'tweet #test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_one_mention_uppercase(self):
        arg = 'tweet @Test case'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_duplicate_mentions_1(self):
        arg = 'tweet @test @Test case'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_duplicate_mentions_2(self):
        arg = 'tweet @test @Test @test case'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'test', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_duplicate_mentions_3(self):
        arg = 'tweet @test @Test case @test'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'test', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_mentions_tags_1(self):
        arg = 'tweet @test @Test case #test @case'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'test', 'case']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_mentions_tags_2(self):
        arg = 'tweet @test @Test case #test #case'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_invalid_mentions_1(self):
        arg = 'tweet @test@Test case #test #case'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_invalid_mentions_2(self):
        arg = 'tweet @test case @!'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_invalid_mentions_3(self):
        arg = 'tweet @test! case @!'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_invalid_mentions_4(self):
        arg = 'tweet @test!@case @!'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_invalid_mentions_5(self):
        arg = 'tweet @test!case @!'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_mention_at_begin(self):
        arg = '@tweet @test!case @!'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_mention_at_end(self):
        arg = 'tweet @test!case @end'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'end']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_mention_at_end_and_begin(self):
        arg = '@tweet @test!case @end'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'test', 'end']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

if __name__ == '__main__':
    unittest.main(exit=False)
