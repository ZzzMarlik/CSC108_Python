import unittest
import twitterverse_functions

class TestFilter(unittest.TestCase):

    def test_username_list_is_empty(self):
        """ Test get_filter_results with empty username-list """

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': '', \
                                   'web': '', 'bio': '', 'following': []}}
        username_list = []
        filter_dic = {'name-includes': 'don'}
        expected_result = []
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)

    def test_filter_username(self):
        """ Test get_filter_results with only username filter """

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': '', \
                                   'web': '', 'bio': '', 'following': []}}
        username_list = ['Sheldon']
        filter_dic = {'name-includes': 'Don'}
        expected_result = ['Sheldon']
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)

    def test_filter_location(self):
        """ Test get_filter_results with only location filter """

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': 'usa', \
                                   'web': '', 'bio': '', 'following': []}}
        username_list = ['Sheldon']
        filter_dic = {'location-includes': 'US'}
        expected_result = ['Sheldon']
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)

    def test_filter_following(self):
        """ Test get_filter_results with only following filter """

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': '', \
                                   'web': '', 'bio': '', 'following': ['mark']}}
        username_list = ['Sheldon']
        filter_dic = {'following': 'MARK'}
        expected_result = []
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)

    def test_filter_follower(self):
        """ Test get_filter_results with only follower filter """

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': '', \
                                   'web': '', 'bio': '', 'following': ['zoe']}}
        username_list = ['Sheldon']
        filter_dic = {'follower': 'mark'}
        expected_result = []
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)

    def test_two_filter(self):
        """ Test get_filter_results with only two filter conditions"""

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': 'usa', \
                                   'web': '', 'bio': '', 'following': ['zoe']}}
        username_list = ['Sheldon']
        filter_dic = {'name-includes': 'Don', 'location-includes': 'US'}
        expected_result = ['Sheldon']
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)        

    def test_three_filter(self):
        """ Test get_filter_results with only three filter conditions"""

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': 'usa', \
                                   'web': '', 'bio': '', 'following': ['zoe']}}
        username_list = ['Sheldon']
        filter_dic = {'name-includes': 'Don', 'location-includes': 'US', \
                      'following': 'mark'}
        expected_result = []
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)  

    def test_three_filter(self):
        """ Test get_filter_results with only three filter conditions"""

        twitter_dic = {'Sheldon': {'name': 'Shuai Shao', 'location': 'usa', \
                                   'web': '', 'bio': '', 'following': ['zoe']}}
        username_list = ['Sheldon']
        filter_dic = {'name-includes': 'Don', 'location-includes': 'US', \
                      'following': 'mark', 'follower': 'zoe'}
        expected_result = []
        result = twitterverse_functions.get_filter_results(twitter_dic, \
                                                  username_list, filter_dic)
        self.assertEqual(expected_result, result)    

if __name__ == '__main__':
    unittest.main(exit=False)