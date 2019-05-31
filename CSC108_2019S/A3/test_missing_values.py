"""A3. Tester for the function patients_with_missing_values
in treatment_functions.
"""

import unittest
import treatment_functions as tfs

ERROR_MESSAGE = "Expected {}, but returned {}"


class TestPatientsWithMissingValues(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def test_empty(self):
        """Empty dictionary."""

        id_to_attributes = {}
        name = 'xyz'
        expected = []
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_one_patient_no_missing(self):
        """One patient, with the value present."""

        id_to_attributes = {
            'Tom':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'}
        }
        name = 'Pet'
        expected = []
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    ### ADD YOUR TESTS HERE ###
    def test_one_patient_one_missing(self):
        """One patient, with the value present."""

        id_to_attributes = {
            'Tom':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'}
        }
        name = 'Car'
        expected = ['Tom']
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_patients_no_missing(self):
        """One patient, with the value present."""

        id_to_attributes = {
            'Tom':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'},
            'Tommy':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'}
        }
        name = 'Pet'
        expected = []
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_patients_some_missing(self):
        """One patient, with the value present."""

        id_to_attributes = {
            'Tom':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'},
            'Lily':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'},
            'Jay':  {'Pet': 'dog', 'Car': 'BMW', 'Team': 'Leafs'}
        }
        name = 'Car'
        expected = ['Tom', 'Lily']
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

if __name__ == '__main__':
    unittest.main(exit=False)
