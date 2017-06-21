"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """convert a dna sequence to RNA."""

    #Determine if the original sequence is upper case
    seq_upper = seq.isupper()

    #convert to lowercase
    seq = seq.lower()

    #swap out 't' for 'u'
    seq = seq.replace ('t', 'u')

    #return upper or lower, depndong on input
    if seq_upper:
        return seq.upper()
    else:
        return seq



def reverse_rna_complement (seq):
    """Convert a DNA sequence into its reverse complement as RNA"""

    #Determine if the original sequence is upper case
    seq_upper = seq.isupper()

    #Reverse the sequence
    seq = seq[::-1]

    #Convert to upper
    seq = seq.upper()

    #Compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    #Return in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq
