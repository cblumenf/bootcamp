import os

if os.path.isfile('gimme_phi.txt'):
    print('Sorry, file exists.')
else:
    with open('gimme_phi.txt', 'w') as f:
        f.write('The golden ratio is ')
        f.write('{phi:.8f}'.format(phi=1.61803398875))
        



"""
import os

if os.path.isfile('mastery.txt'):
    print('Sorry, file exists.')
else:
    with open('mastery.txt', 'w') as f:
        f.write('This is my file.\n')
        f.write('There are many like it, but this one is mine.\n')
        f.write('I must master my file like I must master my life.\n')
"""

"""
with open('data/1OLG.pdb', 'r') as f:
    for i, line in enumerate(f):
        print(line.rstrip())
        if i >= 10:
            break
"""





"""
with open('data/1OLG.pdb', 'r') as f:
    f_lines = f.readlines()
    print('In the with bloc, is the file closed?', f.closed)

print('Out of the with block, is the file closed?', f.closed)

print(f_lines[:3])
"""
