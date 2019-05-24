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

    def test_nonempty_with_invalid_mention(self):
        """Non-empty tweet with invalid mentions."""

        arg = '@! blabla @! blabla @!'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_nonempty_three_mention_in_different_position(self):
        """Non-empty tweet with different positions."""

        arg = '@jesse blabla @JESSE blabla @JesSe'
        actual = tweets.extract_mentions(arg)
        expected = ["jesse", "jesse", "jesse"]
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_nonempty_but_mess(self):
        """Non-empty tweet with mess mentions."""

        arg = '@jess?e? blabla @tho123~mas123 blabla @@je%sse'
        actual = tweets.extract_mentions(arg)
        expected = ["jess", "tho123"]
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

if __name__ == '__main__':
    unittest.main(exit=False)
