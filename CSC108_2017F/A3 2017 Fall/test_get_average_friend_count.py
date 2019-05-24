import unittest
import network_functions

class TestGetAverageFriendCount(unittest.TestCase):

    def test_get_average_empty(self):
        param = {}
        actual = network_functions.get_average_friend_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_get_average_one_person_one_friend(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_average_two_person_three_friend(self):
        param = {'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
            'Dylan D-Money': ['Haley Gwendolyn Dunphy']}
        actual = network_functions.get_average_friend_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        

if __name__ == '__main__':
    unittest.main(exit=False)