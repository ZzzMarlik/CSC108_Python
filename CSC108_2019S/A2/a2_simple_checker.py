"""A simple checker for types of functions in palindromes.py and dna.py."""

from typing import Callable
import sys
sys.path.insert(0, 'pyta')
import python_ta
import palindromes as pals
import dna


##### Generic functions #####

def type_error_message(func_name: str, expected: str, got: str) -> str:
    """Return an error message for function func_name returning type got,
    where the correct return type is expected.
    """

    return ('{} should return a {}, but returned {}' +
            '.').format(func_name, expected, got)


def check_function(func: Callable, args: list, ret_type: type) -> None:
    """Check that func called with arguments args returns a value of type
    ret_type. Display the progress and the result of the check.
    """

    print('Checking {}...'.format(func.__name__))
    got = func(*args)
    assert isinstance(got, ret_type), \
        type_error_message(func.__name__, ret_type.__name__, type(got))
    print('  check complete')


def check_type_details(assertion: bool, func_name: str, expected: str,
                       got: str) -> None:
    """Check that assertion is True. Display the progress and the result
    of the check. Failure means that function func_name was expected
    to return a value of type expected, but returned a value whose str
    represenation is got.

    Useful when return type is, for example, a nested list.
    """

    print('Checking {}...'.format(func_name))
    assert assertion, type_error_message(func_name, expected, got)
    print('  check complete')


###############
    
print('=====================================================================')
print('=====================================================================')
print('=====================================================================')
print()
print('==================== Checking palindromes.py ========================')

print('==================== Start: checking coding style ===================')

python_ta.check_all('palindromes.py', config='pyta/a2_pyta.txt')

print('=================== End: checking coding style ====================\n')

check_function(pals.is_palindrome_word, ['abracadabra'], bool)
check_function(pals.is_palindrome_phrase, ['abracadabra'], bool)
check_function(pals.get_odd_palindrome_at, ['abracadabra', 4], str)

print('=====================================================================')
print('=====================================================================')
print('=====================================================================')
print()

print('======================== Checking dna.py ============================')

print('==================== Start: checking coding style ===================')

python_ta.check_all('dna.py', config='pyta/a2_pyta.txt')

print('=================== End: checking coding style ====================\n')


print('== Start: checking whether initial values of constants are modified ==')

# Get the initial values of the constants
CONSTS_BEFORE = [dna.CYTOSINE, dna.GUANINE, dna.ADENINE, dna.THYMINE]

print('Check whether the constants are unchanged from the starter code.')

assert CONSTS_BEFORE == ['C', 'G', 'A', 'T'], \
    ('You have modified the value of some constant(s). Edit your code so that'
     + ' the values of constants are the same as in the starter code.')

print('  check complete')

print('== End: checking whether initial values of constants are modified ==\n')


print('============ Start: checking parameter and return types ============')

check_function(dna.is_base_pair, ['A', 'T'], bool)
check_function(dna.are_complementary, ['AT', 'TA'], bool)
check_function(dna.is_dna_palindrome, ['A', 'T'], bool)

got = dna.restriction_sites('GAAGCTGA', 'GA')
check_type_details(
    isinstance(got, list) and got != [] and isinstance(got[0], int),
    'restriction_sites',
    'List[int]',
    str(got))

got = dna.match_enzymes('GGATCCGAAGGAATGGATCCTGAGAATTC', ['EcoRI', 'BamHI'],
                        ['GAATTC', 'GGATCC'])
check_type_details(
    (isinstance(got, list) and got != [] and
     isinstance(got[0], list) and got[0] != [] and
     isinstance(got[0][0], str) and
     isinstance(got[0][1], list) and got[0][1] != [] and
     isinstance(got[0][1][0], int)),
    'match_enzymes',
    'list of two-item [str, List[int]] lists',
    str(got))
     
got = dna.one_cutters('GGATCCGAAGGAATGGATCCTGAGAATTC', ['EcoRI', 'BamHI'],
                      ['GAATTC', 'GGATCC'])
check_type_details(
    (isinstance(got, list) and got != [] and
     isinstance(got[0], list) and got[0] != [] and
     isinstance(got[0][0], str) and isinstance(got[0][1], int)),
    'one_cutters',
    'list of two-item [str, int] lists',
    str(got))

check_function(dna.replace_mutations,
               [['ACGTGGCCTAGCT', 'CAGTGATCG', 'ACATGGGCCGT'],
                'ACGGCCTT', ['HaeIII', 'HgaI', 'AluI'],
                ['GGCC', 'GACGC', 'AGCT']],
               type(None))

print('============= End: checking parameter and return types =============\n')

print('======= Start: checking whether functions modify constants =======')

# Get the final values of the constants
CONSTS_AFTER = [dna.CYTOSINE, dna.GUANINE, dna.ADENINE, dna.THYMINE]

# Check whether the constants are unchanged.
print('Checking whether functions modify constants...')
assert CONSTS_BEFORE == CONSTS_AFTER, \
    ('Your function(s) modified the value of some constant(s). Edit your' +
     '\ncode so that the values of constants are unchanged by your functions.')
print('  check complete')

print('=========== End: checking whether functions modify constants ====')
