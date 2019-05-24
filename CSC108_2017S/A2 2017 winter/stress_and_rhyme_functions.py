# The main module - need to import so that window code works correctly
import annotate_poetry

NO_STRESS_SYMBOL = 'x'
PRIMARY_STRESS_SYMBOL = '/'
SECONDARY_STRESS_SYMBOL = '\\'  # note: len('\\') == 1 due to special character

"""
A pronouncing table: a nested list, [list of str, list of list of str]
  o a two item list, contains two parallel lists
  o the first item is a list of words (each item in this sublist is a str
    for which str.isupper() is True)
  o the second item is a list of pronunciations, where a pronunciation is a
    list of phonemes (each item in this sublist is a list of str)
  o the pronunciation for the word at index i in the list of words is at index
    i in the list of pronunciations
"""

# A small pronouncing table that can be used in docstring examples.
SMALL_TABLE = [['A', 'BOX', 'CONSISTENT', 'DON\'T', 'FOX', 'IN', 'SOCKS'],
               [['AH0'],
                ['B', 'AA1', 'K', 'S'],
                ['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'],
                ['D', 'OW1', 'N', 'T'],
                ['F', 'AA1', 'K', 'S'],
                ['IH0', 'N'],
                ['S', 'AA1', 'K', 'S']]]

# A small poem that can be used in docstring examples.
SMALL_POEM = "\nI'll sit here instead,\n\n\n\nA cloud on my head\n\n"

"""
A pronouncing dictionary is a list of pronouncing lines, where a pronouncing
line is a line in the CMU Pronouncing Dictionary format:
  a word followed by the phonemes describing how to pronounce the word.
  o example:
    BOX  B AA1 K S
"""

# A small pronouncing dictionary that can be used in docstring examples.
SMALL_PRONOUNCING_DICT = [
    'A AH0',
    'BOX B AA1 K S',
    'CONSISTENT K AH0 N S IH1 S T AH0 N T',
    'DON\'T D OW1 N T',
    'FOX F AA1 K S',
    'IN IH0 N',
    'SOCKS S AA1 K S']

# ===================== Provided Helper Functions =============================


def prepare_word(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been converted to
    uppercase and punctuation characters have been stripped from both ends.
    Inner punctuation is left unchanged.

    This function prepares a word for looking up in a pronouncing table.

    >>> prepare_word('Birthday!!!')
    'BIRTHDAY'
    >>> prepare_word('"Quoted?"')
    'QUOTED'
    >>> prepare_word("Don't!")
    "DON'T"
    """

    punctuation = """!"`@$%^&_+-={}|\\/—,;:'.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


def get_rhyme_scheme_letter(offset):
    """ (int) -> str

    Precondition: 0 <= offset <= 25

    Return the letter corresponding to the offset from 'A'.  Helpful when
    labelling a poem with its rhyme scheme.

    >>> get_rhyme_scheme_letter(0)
    'A'
    >>> get_rhyme_scheme_letter(25)
    'Z'
    """

    return chr(ord('A') + offset)


# ======== Students: Add Any Helper Functions Below This Line ================
def get_rhyme_scheme_list(poem_lines, pronouncing_table):
    """ (list of str, pronouncing table) -> list of list of str

    Return a list of list of string that shows the rhyme scheme of each
    poem_lines corresponding to the pronouncing_table.

    >>> pronouncing_table = SMALL_TABLE
    >>> poem_lines = ["Don't, in box!", '', 'Fox in socks.', 'Consistent.']
    >>> get_rhyme_scheme_list(poem_lines, pronouncing_table)
    [['AA1', 'K', 'S'], ' ', ['AA1', 'K', 'S'], ['AH0', 'N', 'T']]
    >>> poem_lines = []
    >>> get_rhyme_scheme_list(poem_lines, pronouncing_table)
    []
    """
    rhyme_scheme = []
    for i in poem_lines:
        if i == '':
            rhyme_scheme.append(' ')
        else:
            last_word = prepare_word(i.split()[-1])
            rhyme_scheme.append(last_syllable(look_up_pronunciation
                                              (last_word, pronouncing_table)))
    return rhyme_scheme


# ======== Students: Add Any Helper Functions Above This Line ================

# ======== Students: Add One Docstring Example And Function ===================
# ========           Body Code To Each Function Below       ===================

def get_word(pronouncing_line):
    """ (str) -> str

    Precondition: pronouncing_line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return the word in pronouncing_line.

    >>> get_word('ABALONE  AE2 B AH0 L OW1 N IY0')
    'ABALONE'
    >>> get_word('BOX B AA1 K S')
    'BOX'
    """
    return pronouncing_line.split()[0]


def get_pronunciation(pronouncing_line):
    """ (str) -> list of str

    Precondition: pronouncing_line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return a list containing the phonemes in pronouncing_line.

    >>> get_pronunciation('ABALONE  AE2 B AH0 L OW1 N IY0')
    ['AE2', 'B', 'AH0', 'L', 'OW1', 'N', 'IY0']
    >>> get_pronunciation('BOX B AA1 K S')
    ['B', 'AA1', 'K', 'S']
    """
    return pronouncing_line.split()[1:]


def make_pronouncing_table(pronouncing_list):
    """ (list of str) -> pronouncing table

    Precondition: pronouncing_list is a list of pronouncing lines.
                  Each pronuncing line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return a pronouncing table for the data in pronouncing_list.

    >>> SMALL_TABLE == make_pronouncing_table(SMALL_PRONOUNCING_DICT)
    True
    >>> [['ASLEEP'], [['AHO', 'S', 'L', 'IY1', 'P']]] \
    == make_pronouncing_table(['ASLEEP AHO S L IY1 P'])
    True
    """
    words = []
    pronunciation = []
    for i in pronouncing_list:
        words.append(get_word(i))
        pronunciation.append(get_pronunciation(i))
    return [words, pronunciation]


def look_up_pronunciation(word, pronouncing_table):
    """ (str, pronouncing table) -> list of str

    Return the list of phonemes for pronouncing word, as found in
    pronouncing_table.  Ignore the leading and trailing punctuation in word
    as well as the case of any letters in word.

    >>> pronouncing_table = SMALL_TABLE
    >>> look_up_pronunciation("Don't!", pronouncing_table)
    ['D', 'OW1', 'N', 'T']
    >>> look_up_pronunciation("SOCKS?!", pronouncing_table)
    ['S', 'AA1', 'K', 'S']
    """
    formal_word = prepare_word(word)
    if formal_word in pronouncing_table[0]:
        index = pronouncing_table[0].index(formal_word)
        return pronouncing_table[1][index]


def is_vowel_phoneme(s):
    """ (str) -> bool

    Return True if and only if s is a vowel phoneme.  Vowel phonemes are three
    character strings that start with two uppercase letters and end with a
    single digit of 0, 1 or 2.  The first uppercase letter must be one of
    A, E, I, O or U.

    >>> is_vowel_phoneme("AE0")
    True
    >>> is_vowel_phoneme('IH1')
    True
    """
    return (len(s) == 3) and (s[0] in 'AEIOU') and (s[1].isupper()) and \
           (s[2] in '012')


def last_syllable(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and any subsequent consonant phoneme(s) from
    phoneme_list, in the same order as they appear in phoneme_list.

    >>> last_syllable(['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'])
    ['AH0', 'N', 'T']
    >>> last_syllable(['IH0', 'N'])
    ['IH0', 'N']
    """
    index = len(phoneme_list) - 1
    while index >= 0:
        if is_vowel_phoneme(phoneme_list[index]):
            return phoneme_list[index:]
        else:
            index -= 1


def convert_to_lines(poem):
    r""" (str) -> list of str

    Return a list of the lines in poem, with leading and trailing whitespace
    removed from each poem line, and leading and trailing blank lines removed.
    Blank lines between stanzas are reduced to a single blank line.

    >>> convert_to_lines(SMALL_POEM)
    ["I'll sit here instead,", '', 'A cloud on my head']
    >>> convert_to_lines('\nOne,\n\n\ntwo,\nthree.\n\n')
    ['One,', '', 'two,', 'three.']
    """
    line = poem.strip()
    acc = ''
    i = 0
    while i < len(line):
        if line[i] != '\n':
            acc += line[i]
        if line[i] == '\n' and line[i + 1] != '\n' and line[i - 1] != '\n':
            acc += '\n'
        elif line[i] == '\n' and line[i + 1] != '\n':
            acc += '\n\n'
        i += 1
    return acc.split('\n')


def detect_rhyme_scheme(poem_lines, pronouncing_table):
    """ (list of str, pronouncing table) -> list of str

    Return a list of single characters indicating the rhyme scheme for
    poem_lines, with blank lines that separate stanzas given the rhyme scheme
    marker ' '.  The marker for the first line in the poem is 'A'. When
    annotating the rhyme scheme in a poem, consecutive uppercase letters are
    used, starting with the letters A, B, C, etc

    >>> pronouncing_table = SMALL_TABLE
    >>> poem_lines = ["Don't, in box!", '', 'Fox in socks.', 'Consistent.']
    >>> detect_rhyme_scheme(poem_lines, pronouncing_table)
    ['A', ' ', 'A', 'B']
    >>> poem_lines = ["Don't, in box!", '', 'Consistent', 'Fox in socks.']
    >>> detect_rhyme_scheme(poem_lines, pronouncing_table)
    ['A', ' ', 'B', 'A']
    """
    rhyme_scheme = get_rhyme_scheme_list(poem_lines, pronouncing_table)
    index = 0
    num = 0
    while index < len(rhyme_scheme):
        temp = rhyme_scheme[index]
        if len(temp) > 1 or len(temp[0]) > 1:
            for item in rhyme_scheme:
                if item == temp:
                    rhyme_scheme[rhyme_scheme.index(item)] \
                        = get_rhyme_scheme_letter(num)
            num += 1
        index += 1
    return rhyme_scheme


def get_stress_pattern(word, pronouncing_table):
    """ (str, pronouncing table) -> str

    Return the stress pattern for pronouncing word using the pronouncing table
    pronouncing_table.  Separate each stress symbol in the stress pattern by a
    single space, and pad the end of the stress pattern with spaces to make
    the length of the stress pattern the same as the length of word.

    The stress symbols are given by the defined constants NO_STRESS_SYMBOL,
    PRIMARY_STRESS_SYMBOL, and SECONDARY_STRESS_SYMBOL, which correspond to
    the lexical stress markers 0, 1 and 2, respectively.

    The docstring examples assume NO_STRESS_SYMBOL = 'x',
    PRIMARY_STRESS_SYMBOL = '/' and SECONDARY_STRESS_SYMBOL = '\\'.

    >>> pronouncing_table = SMALL_TABLE
    >>> get_stress_pattern('consistent', pronouncing_table)
    'x / x     '
    >>> get_stress_pattern('box?', pronouncing_table)
    '/   '
    """
    acc = ''
    pronounciation = look_up_pronunciation(word, pronouncing_table)
    for i in pronounciation:
        if is_vowel_phoneme(i):
            if i[-1] == '0':
                acc += (NO_STRESS_SYMBOL + ' ')
            if i[-1] == '1':
                acc += (PRIMARY_STRESS_SYMBOL + ' ')
            if i[-1] == '2':
                acc += (SECONDARY_STRESS_SYMBOL + ' ')
    while len(acc) < len(word):
        acc += ' '
    return acc


if __name__ == '__main__':
    import doctest
    doctest.testmod()
