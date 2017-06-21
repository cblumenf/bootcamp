

def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence of nucleotides."""

    #Initialize the complement
    comp_seq = ''

    for base in seq:
        comp_seq += complement_base(base, material=material)

    #Returns reverse complement
    return comp_seq[::-1]

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
