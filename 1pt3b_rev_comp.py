
def reverse_complement(seq, material='DNA'):
    """Computes reverse complement of a sequence."""

    #Convert sequence to uppercase
    upper_sequence = seq.upper()

    #Exchanges bases with lower case complement
    if material == 'DNA':
        upper_sequence = upper_sequence.replace("A", "t")
        upper_sequence = upper_sequence.replace("T", "a")
        if upper_sequence.find("U") != -1:
            print("This is not DNA.")
            return "Error"
    elif material == 'RNA':
        upper_sequence = upper_sequence.replace("A", "u")
        upper_sequence = upper_sequence.replace("U", "a")
        if upper_sequence.find("T") != -1:
            print('This is not RNA.')
            return "Error"
    upper_sequence = upper_sequence.replace("G", "c")
    upper_sequence = upper_sequence.replace("C", "g")
    upper_sequence = upper_sequence.upper()
    reversed_sequence = upper_sequence[::-1]
    return reversed_sequence
