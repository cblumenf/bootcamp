import os

def fasta_stapler(fasta_file):
    """
    This function takes in a fasta file, removes the first line,
    and provides a stapled, single string.
    """
    with open(fasta_file, 'r') as f:

        #Read contents in as a list
        f_lines = f.readlines()

    #Initialize stapled string
    stapled = ''

    #Shorten list to remove top line
    f_shortened = f_lines[1:]

    for line in f_shortened:
        stapled += line.rstrip()

    return stapled
