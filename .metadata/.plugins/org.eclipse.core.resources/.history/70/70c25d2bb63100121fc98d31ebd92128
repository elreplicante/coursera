def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
     
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1) > len(dna2)




def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    return dna.count(nucleotide)
    



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna1.count(dna2) > 0

def is_valid_sequence(sequence):
    '''(str) -> bool
    
    The parameter is a potential DNA sequence.
    Return True if and only if the DNA sequence 
    is valid (that is, it contains only nucleotide 
    characters: 'A', 'T', 'C' and 'G'). 
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('AtCgGC')
    False
    >>> is_valid_sequence('ATCGRGC')
    False
    
    '''
    for char in sequence:
        if char not in 'ATCG':
            return False
    return True

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str
    
    The first two parameters are DNA sequences and 
    the third parameter is an index. 
    Return the DNA sequence obtained by inserting the 
    second DNA sequence into the first DNA sequence at 
    the given index. (You can assume that the index is valid.)   
      
    >>> insert_sequence('CCGG', 'AT')
    'CCATGG'
    
    '''
    
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    '''(str) -> str
    
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G').
    Return the nucleotide's complement. 
    
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    
def get_complementary_sequence(sequence):
    '''(str) -> str
    
    The parameter is a DNA sequence. 
    Return the DNA sequence that is complementary 
    to the given DNA sequence.  
    
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGAATGCCTA')
    'GCTTACGGAT'
    
    '''
    complement_sequence = '' 
    for char in sequence:
        complement_sequence = complement_sequence + get_complement(char)
    
    return complement_sequence
    