start_codon = "AUG"

seq = 'GUGGGGGAACCAAGAUGCCCGGAAGACCAAGGAGC'

# Initialize sequence index
i = 0

# Scan the seqeunce until start codon
while seq[i:i+3] != start_codon and i < len(seq):
    i += 1

if i == len(seq):
    print('Start codon not found')
else:
    print ('start codon at index', i)
