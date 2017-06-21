def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence."""

    #Initialize the reverse complement
    rev_seq = ''

    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)

    return rev_seq

def complement_base(base, material='DNA'):
    """Returns the Waston-Crick copmplement of a base."""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

    print ('I love bootcamp.')
