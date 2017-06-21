def common_str_finder(str1, str2):
    """This function takes in two strings and finds the longest common
    substring."""

    str1_list = list(str1)
    str2_list = list(str2)

    if len(str1) <= len(str2):
        shortlist = str1
        longlist = str2
    else:
        shortlist = str2
        longlist = str1



    print(len(shortlist))
    print(len(longlist))


###What I need to do:
    """I must find which is shorter and which is longer.  Then I must search
    for the shorter in the longer.  If I find a longest common subsequence
    I must print this sequence.  If I do not, I must indicate it."""
