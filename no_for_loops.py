
def reverse_gen(seq):
    """This function takes in a sequence of DNA and replaces it with its
    complement."""

    my_complement = seq[::-1]
    my_complement = seq.replace("A", "t")
    my_complement = my_complement.replace("T", "a")
    my_complement = my_complement.replace("G", "c")
    my_complement = my_complement.replace("C", "g")
    my_finalcomplement = my_complement.upper()


    return my_revcomplement
