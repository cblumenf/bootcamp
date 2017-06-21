import os

with open ('~/git/bootcamp/data/salmonella_spi1_region.fna', 'r') as f:

    #Read contents in as a list
    f_lines = f.readlines()
    print('In the with block, is the closed?', f.closed)

    #

print('Out of the with block, is the file closed?', f.closed)
