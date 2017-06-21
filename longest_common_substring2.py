def common_str_finder(str1, str2):
    """This function takes in two strings and finds the longest common
    substring."""

    ###determines which list is the shortest and which is the longest.
    if len(str1) <= len(str2):
        shortstr = str1
        longstr = str2
    else:
        shortstr = str2
        longstr = str1

    longerlen = len(longstr)
    longerlist = list(range(longerlen))

    for i in longerlist:
        
    #print(longerlist)


    print(len(shortstr))
    print(len(longstr))


###What I need to do:
    """I must find which is shorter and which is longer.  Then I must search
    for the shorter in the longer.  If I find a longest common subsequence
    I must print this sequence.  If I do not, I must indicate it."""
