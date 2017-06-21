#base = input('Please input your bases: ')
#material = input('Please input your material: ')



def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

#create empty string
def reverse_complement(seq, material='DNA'):
    """This will compute the reverse complement of the DNA sequence"""

#empty list
    rev_compstr = ''

    for base in seq[::-1]:
        rev_compstr += complement_base(base, material=material)

    return rev_compstr
