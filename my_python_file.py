

start_codon = 'AUG'
stop_codons = ('UAA', 'UAG', 'UGA')

codon = "UAG"

if codon == start_codon:
    print ('This codon is the start codon.')
elif codon in stop_codons:
    print('This codon is a stop codon.')
else:
    print ('This codon is not the start or stop codon.')
