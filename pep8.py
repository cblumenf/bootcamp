#before
"""
seq='AUCUGUACUAAUGCUCAGCACGACGUACG'
c='AUG'  # This is the start codon
i =0  # Initialize sequence index
while seq[ i : i + 3 ]!=c:
    i+=1

print('The start codon starts at index', i)
"""

#after!
start_codon = 'AUG'

# Initialize sequence index for while loop
i = 0

# Scan sequence until we hit the start codon
while seq[i:i+3] != start_codon:
    i += 1

print('The start codon starts at index', i)
