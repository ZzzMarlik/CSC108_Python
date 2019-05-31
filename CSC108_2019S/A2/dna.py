"""Assignment 2: DNA Manipulation"""

from typing import List
import palindromes


CYTOSINE = 'C'
GUANINE = 'G'
ADENINE = 'A'
THYMINE = 'T'


####### BEGIN PROVIDED HELPER FUNCTION ####################

def get_complementary_base(base: str) -> str:
    """Return the complement of base.

    Precondition: base in 'ATCG', base is not empty

    >>> get_complementary_base('A')
    'T'
    >>> get_complementary_base('C')
    'G'
    """

    if base == ADENINE:
        return THYMINE
    elif base == THYMINE:
        return ADENINE
    elif base == CYTOSINE:
        return GUANINE
    else:  # base == GUANINE
        return CYTOSINE


####### END PROVIDED HELPER FUNCTION ####################
def is_base_pair(s1: str, s2: str) -> bool:
    """Return True if and only if the two parameters form a base pair.
    
    >>> is_base_pair('A', 'T')
    True
    >>> is_base_pair('G', 'C')
    True
    >>> is_base_pair('G', 'A')
    False
    """
    return s1 == get_complementary_base(s2)

def are_complementary(s1: str, s2: str) -> bool:
    """Return True if and only if the two strands are complementary.
    
    >>> are_complementary("ATC", "ATC")
    False
    >>> are_complementary("ATC", "TAG")
    True
    """
    for i in range(len(s1)):
        if not is_base_pair(s1[i], s2[i]):
            return False
    return True

def is_dna_palindrome(s1: str, s2: str) -> bool:
    """Return True if and only if the DNA strands represented
    by the two parameters form a DNA palindrome.
    
    >>> is_dna_palindrome("GGATCC", "CCTAGG")
    True
    >>> is_dna_palindrome("GGC", "CCG")
    False
    """
    return palindromes.is_palindrome_word(s1+s2)

def restriction_sites(dna: str, seq: str) -> List[int]:
    """Return a list of all the indices where the recognition sequence
    appears in the DNA strand. (These are the restriction sites.)
    
    >>> restriction_sites('GGATCC', 'AA')
    []
    >>> restriction_sites('GGATCC', 'CC')
    [4]
    >>> restriction_sites('GGGG', 'GG')
    [0, 1, 2]
    """
    acc = []
    start = dna.find(seq)
    if start == -1:
        return acc
    else:
        acc.append(start)
        while start != -1:
            start = dna.find(seq, start + 1)
            if start != -1:
                acc.append(start)
    return acc

def match_enzymes(dna: str, name: List[str], seq: List[str]) -> List[list]:
    """Return a list of two-item lists where the first item of each two-item
    list is the name of a restriction enzyme and the second item is the list of
    indices (in the DNA strand) of the restriction sites that the enzyme cuts.
    
    >>> match_enzymes('TCGATCGAGGCC', ['TaqI', 'HaeIII'], ['TCGA', 'GGCC'])
    [['TaqI', [0, 4]], ['HaeIII', [8]]]
    >>> match_enzymes('GAATTCGA', ['EcoRI','TaqI','Sau3A'], ['GAATTC','TCGA','GATC'])
    [['EcoRI', [0]], ['TaqI', [4]], ['Sau3A', []]]
    """
    acc = []
    for item in seq:
        seq_name = name[seq.index(item)]
        occ = restriction_sites(dna, item)
        acc.append([seq_name, occ])
    return acc

def one_cutters(dna: str, name: List[str], seq: List[str]) -> List[list]:
    """Return a list of two-item lists representing the 1-cutters formed by
    restriction_enzyme and recognition_sequences for the DNA strand.
    
    >>> one_cutters('TCGATCGAGGCC', ['TaqI', 'HaeIII'], ['TCGA', 'GGCC'])
    [['HaeIII', 8]]
    >>> one_cutters('GAATTCGA', ['EcoRI','TaqI','Sau3A'], ['GAATTC','TCGA','GATC'])
    [['EcoRI', 0], ['TaqI', 4]]
    """
    acc = match_enzymes(dna, name, seq)
    new = []
    i = 0
    while i < len(acc):
        if len(acc[i][1]) == 1:
            new.append([acc[i][0], acc[i][1][0]])
        i += 1
    return new

def replace_mutations(mute: List[str], clean: str,
                      name: List[str], seq: List[str]) -> None:
    """Modifies the list of mutated strands that share a 1-cutter with the
    clean strand by replacing all bases starting at the 1-cutter in the
    mutated strand with all bases starting at the 1-cutter in the clean
    strand, up to and including the end of the strand.
    
    >>> t1 = ['GGCTCGA', 'AGGCC']
    >>> replace_mutations(t1, 'TCGAGGCCTT', ['TaqI', 'HaeIII'], ['TCGA', 'GGCC'])
    >>> t1 == ['GGCTCGAGGCCTT', 'AGGCCTT']
    True
    >>> t2 = ['GGCTCGATCGA', 'AGGCC']
    >>> replace_mutations(t2, 'AAAA', ['TaqI', 'HaeIII'], ['TCGA', 'GGCC'])
    >>> t2 == ['GGCTCGATCGA', 'AGGCC']
    True
    >>> strands = ['ACGTGGCCTAGCT', 'CAGCTGATCG']
    >>> clean = 'ACGGCCTT'
    >>> names = ['HaeIII', 'HgaI', 'AluI']
    >>> sequences = ['GGCC', 'GACGC', 'AGCT']
    >>> replace_mutations(strands, clean, names, sequences)
    >>> strands
    ['ACGTGGCCTT', 'CAGCTGATCG']
    """
    clean_cut = one_cutters(clean, name, seq)
    for i in range(len(mute)):
        temp = one_cutters(mute[i], name, seq)
        d = {}
        for item in temp:
            d[item[0]] = item[1]
        cut = []
        for item in clean_cut:
            if item[0] in d:
                cut = [item[1], d[item[0]]] #[clean_lst, mute_lst]
        if cut != []:
            mute[i] = mute[i][:cut[1]] + clean[cut[0]:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
