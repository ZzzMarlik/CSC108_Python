def is_base_pair(str1, str2):
    '''(str, str) -> bool

    Return True iff str1 and str2 can form a base pair

    >>>is_base_pair('A', 'T')
    True
    >>>is_base_pair('A', 'C')
    False
    '''
    if ((str1 == 'A' and str2 == 'T') or (str1 == 'T' and str2 == 'A') or
        (str1 == 'G' and str2 == 'C') or (str1 == 'C' and str2 == 'G')):
        return True
    else:
        return False

def is_dna(strand1, strand2):
    '''(str, str) -> bool

    Pre-condition: len(strand1) == len(strand2) == 4 and strands only contains
    'A', 'T', 'G', 'C'.

    Return True iff strand1 and strand2 form a properly base-paired DNA
    molecule

    >>>is_dna('GGTC', 'CCAG')
    True
    >>>is_dna('GGTC', 'CCAA')
    False
    '''
    i = 0
    while i < len(strand1):
        if not is_base_pair(strand1[i], strand2[i]):
            return False
        i += 1
    return True

def is_dna_palindrome(strand1, strand2):
    '''(str, str) -> bool

    Pre-condition: is_dna(strand1, strand2) == True

    Return True iif strand1 and strand2 form a DNA palindrome

    >>>is_dna_palindrome('GGATCC', 'CCTAGG')
    True
    >>>is_dna_palindrome('GGATC', 'CCTAG')
    Fasle
    '''
    return strand1+strand2 == (strand1+strand2)[::-1]

def restriction_sites(strand, recognition_sequences):
    '''(str, str) -> list of int

    Return a list of all the indices where the recognition_sequence appears
    in the strand.

    >>>restriction_sites('GGATC', 'GG')
    [0]
    >>>restriction_sites('GGATGGTAGG', 'GG')
    [0, 4, 8]
    >>>restriction_sites('GGGGAATT', 'GG')
    [0, 2]
    >>>restriction_sites('GGGGAATT', 'CC')
    []
    >>>restriction_sites('TCGAAGCTCGAGGCC', 'GGCC')
    [11]
    '''
    i = 0
    acc = []
    if recognition_sequences in strand:
        while i > -1:
            y = strand.find(recognition_sequences, i)
            acc.append(y)
            x = y + len(recognition_sequences)
            i = strand.find(recognition_sequences, x)
    return acc

def match_enzymes(strand, restriction_enzyme, recognition_sequences):
    '''(str, list of str, list of str) -> list of two-item [str, list of int]
    lists

    Return a list of two-item lists where the first item of each two-item list
    is the name of a restriction_enzyme and the second item is the list of
    indices (in the DNA strand) of the restriction sites that the enzyme cuts
    from the revognition_sequences.

    >>>match_enzymes('TCGAAGCTCGAGGCC', ['TaqI', 'HaeIII'], ['TCGA', 'GGCC'])
    [['TaqI', [0, 7]], ['HaeIII', [11]]]
    >>>match_enzymes('ATCGGCATTCGATGACGCTCGA', ['HGaI','TAqI','BamHI'],
    ['GACGC','TCGA','GGATCC'])
    [['HGaI', [13]], ['TAqI', [8, 18]], ['BamHI', []]]
    '''
    acc = []
    i = 0
    while i < len(recognition_sequences):
        X = [(restriction_enzyme[i]),
             (restriction_sites(strand, recognition_sequences[i]))]
        acc.append(X)
        i += 1
    return acc

def one_cutters(strand, restriction_enzyme, recognition_sequences):
    '''(str, list of str, list of str) -> list of two-item [str, int] lists

    Return a list of two-item lists representing the 1-cutters formed by
    restriction_enzyme and recognition_sequences for the DNA strand.

    >>>one_cutters('TCGAAGCTCGAGGCC', ['TaqI', 'HaeIII'], ['TCGA', 'GGCC'])
    [['HaeIII', 11]]
    >>>one_cutters('ATCGGCATTCGATGACGCTCG', ['HGaI','TAqI','BamHI'],
    ['GACGC','TCGA','GGATCC'])
    [['HGaI', 13], ['TAqI', 8]]
    '''
    acc = []
    i = 0
    while i < len(recognition_sequences):
        Y = (restriction_sites(strand, recognition_sequences[i]))
        if len(Y) == 1:
            X = [(restriction_enzyme[i]), Y[0]]
            acc.append(X)
        i += 1
    return acc

def correct_mutations(mutated_dna, clean_strand, restriction_enzyme,
                      recognition_sequences):
    '''(list of str, str, list of str, list of str) -> NoneType

    Modifies the list of mutated_dna that share a 1-cutter(formed by
    restriction_enzyme and recognition_sequences) with the clean_strand by
    replacing all bases starting at the 1-cutter in the mutated_dna with
    all bases starting at the 1-cutter in the clean_strand,up to and including
    the end of the strand.

    >>>correct_mutations(['ACGTGGCCTAGCT', 'CAGCTGATCG'], 'ACGGCCTT',
    ['HaeIII', 'HgaI', 'AluI'], ['GGCC', 'GACGC', 'AGCT'])
    mutated_dna = ['ACGTGGCCTT', 'CAGCTGATCG']
    >>>correct_mutations(['ACTGACGCAA', 'ACTAGCTT'], 'AGCTCGACGCT',
    ['AluI', 'HgaI'], ['AGCT', 'GACGC'])
    mutated_dna = ['ACTGACGCT', 'ACTAGCTCGACGCT']
    >>>correct_mutations(['GCTCTAGAATC', 'GATCTTCTAGAGC'], 'GTCTAGACC',
    ['PstI', 'XbaI', 'Sau3A'], ['CTGCAG', 'TCTAGA', 'GATC'])
    mutated_dna = ['GCTCTAGACC', 'GATCTTCTAGACC']
    '''
    i = 0
    while i < len(mutated_dna):
        j = 0
        while j < len(recognition_sequences):
            x = one_cutters(mutated_dna[i], [restriction_enzyme[j]],
                            [recognition_sequences[j]])
            z = one_cutters(clean_strand, [restriction_enzyme[j]],
                            [recognition_sequences[j]])
            if x != [] and z != []:
                y = x[0][1]
                a = z[0][1]
                mutated_dna[i] = mutated_dna[i][:y] + clean_strand[a:]
            j += 1
        i += 1
