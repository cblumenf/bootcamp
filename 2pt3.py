def gc_blocks(seq, block_size):
    """
    This function takes in a sequence and a block size,
    and computes the GC content.
    """

    #Initialize an empty list which will have content
    content_list = []

    #This loop splits the sequence into blocks
    for x in range(0, len(seq), block_size):
        content_list.append(seq[x:x+block_size])

    GC_block_content = []

    #Computes GC content for each block
    for sequence in content_list:
        GC_block_content.append(gc_content(sequence))


    return tuple(GC_block_content)


def gc_content(sequence):
    """
    This function takes in a sequence and returns GC content.
    """

    sequence_length = len(sequence)
    GC_count = sequence.count("G") + sequence.count("C")
    return GC_count/sequence_length


def gc_map(seq, block_size, gc_thresh):
"""
This function compares the GC content in a block to a GC threshold
and if the block is lower in content, the block will be lower
cased.
"""
    #Initializes the studied sequence
    studied_string = ''

    for element in gc_blocks(seq, block_size):
        if gc_thresh < element:
            studied_string += .lower()
