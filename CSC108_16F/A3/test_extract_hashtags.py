import unittest
import tweets


class TestExtractHashtags(unittest.TestCase):

    def test_no_hashtags(self):
        """ Test extract_hashtags with a tweet with no hashtags. """

        actual_hashtags = tweets.extract_hashtags('this is a tweet!')
        expected_hashtags = []
        self.assertEqual(actual_hashtags, expected_hashtags, 'empty list')

    # Place your unit test definitions after this line.

    def test_only_hashtags(self):
        """ Test extract_hashtags with a tweet with only hashtag. """

        actual_hashtags = tweets.extract_hashtags('###')
        expected_hashtags = ['']
        self.assertEqual(actual_hashtags, expected_hashtags, [''])

    def test_beginning_hashtags(self):
        """ Test extract_hashtags with a tweet with hashtag at the beginning. """

        actual_hashtags = tweets.extract_hashtags('#CSC108')
        expected_hashtags = ['CSC108']
        self.assertEqual(actual_hashtags, expected_hashtags, ['CSC108'])

    def test_middle_hashtags(self):
        """ Test extract_hashtags with a tweet with hashtag at the middle. """

        actual_hashtags = tweets.extract_hashtags('Love #CSC108 forever')
        expected_hashtags = ['CSC108']
        self.assertEqual(actual_hashtags, expected_hashtags, ['CSC108'])

    def test_end_hashtags(self):
        """ Test extract_hashtags with a tweet with hashtag at the end. """
        
        actual_hashtags = tweets.extract_hashtags('I LOVE #CSC108')
        expected_hashtags = ['CSC108']
        self.assertEqual(actual_hashtags, expected_hashtags, ['CSC108'])

    def test_hashtags_with_space(self):
        """ Test extract_hashtags with a tweet with hashtag with space. """

        actual_hashtags = tweets.extract_hashtags('#CSC148 #CSC108')
        expected_hashtags = ['CSC148', 'CSC108']
        self.assertEqual(actual_hashtags, expected_hashtags, 
                         ['CSC148', 'CSC108'])

    def test_hashtags_with_punctuation(self):
        """ Test extract_hashtags with a tweet with hashtag with punctuation. """
        
        actual_hashtags = tweets.extract_hashtags('#CSC148, #CSC108')
        expected_hashtags = ['CSC148', 'CSC108']
        self.assertEqual(actual_hashtags, expected_hashtags, 
                         ['CSC148', 'CSC108'])  

    def test_same_hashtags(self):
        """ Test extract_hashtags with a tweet with same hashtags. """
        
        actual_hashtags = tweets.extract_hashtags('#CSC108, #CSC108')
        expected_hashtags = ['CSC108']
        self.assertEqual(actual_hashtags, expected_hashtags, ['CSC108'])

    def test_hashtags_with_normal_tweet(self):
        """ Test extract_hashtags with a normal tweet with hashtag. """
        
        actual_hashtags = tweets.extract_hashtags('While Hillary profits off the rigged system, I am fighting for you! Remember the simple phrase: #FollowTheMoney... https://t.co/8mVInc82E9')
        expected_hashtags = ['FollowTheMoney']
        self.assertEqual(actual_hashtags, expected_hashtags, ['FollowTheMoney'])       
    
# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
