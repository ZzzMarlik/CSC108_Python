import unittest
from flight_functions import is_valid_flight_sequence

# You can use this data in your tests if you want to
SMALL_ROUTES_DICT = {'AA1': {'AA2', 'AA3'}}
TEST_ROUTES_DICT_FOUR_CITIES = {
    'AA1': {'AA2', 'AA4'},
    'AA2': {'AA3'},
    'AA3': {'AA4', 'AA1'},
    'AA4': {'AA1'}}

# You can (and should) also create and use other RouteDicts for your tests

class TestIsValidFlightSequence(unittest.TestCase):

    def test_valid_direct_flight(self):
        expected = True
        sequence = ['AA1', 'AA2']
        actual = is_valid_flight_sequence(sequence, SMALL_ROUTES_DICT)
        self.assertEqual(actual, expected)
        
    # Add tests below to create a complete set of tests without redundant tests
    # Redundant tests are tests that would only catch bugs that another test
    # would also catch.
    def test_valid_not_direct_flight(self):
        expected = False
        sequence = ['AA2', 'AA4']
        actual = is_valid_flight_sequence(sequence, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        expected = False
        sequence = []
        actual = is_valid_flight_sequence(sequence, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)

    def test_only_one_valid_flight(self):
        expected = True
        sequence = ['AA2']
        actual = is_valid_flight_sequence(sequence, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
    
    def test_only_one_not_valid_flight(self):
        expected = False
        sequence = ['BB2']
        actual = is_valid_flight_sequence(sequence, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)
        
    def test_not_valid_flight(self):
        expected = False
        sequence = ['AA2', 'AA3', 'BB2']
        actual = is_valid_flight_sequence(sequence, TEST_ROUTES_DICT_FOUR_CITIES)
        self.assertEqual(actual, expected)        
        
if __name__ == '__main__':
    unittest.main(exit=False)
