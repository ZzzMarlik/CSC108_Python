import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_get_families_one_person_one_friend_same_family(self):
        param = {'Jay Dunphy': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Claire', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_get_families_with_long_first_name_and_dash(self):
        param = {'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
             'Dylan D-Money': ['Haley Gwendolyn Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Dunphy': ['Haley Gwendolyn'],
                    'D-Money': ['Dylan'], 'D-Cat': ['Gilbert']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

if __name__ == '__main__':
    unittest.main(exit=False)