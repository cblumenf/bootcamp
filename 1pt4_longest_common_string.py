def longest_common_string(string1, string2):
    """Computes the longest common substring for two substrings."""

    #Determines which is the shortest string and makes that string1
    if len(string1) > len(string2):
        string1, string2 = string2, string1

    #determines the length of substring so it can be reduced with each iteration
    substring_length = len(string1)

    #Creates iterative sequence to reduce down substring length after pass
    while substring_length > 0:

        #Try each substring in string1 by testing on string 2 (large to small)
        for substring in range(len(string1) - substring_length + 1):
            if string1[substring:substring + substring_length] in string2:
                return string1[substring:substring+substring_length]

        #Shortens the substring
        substring_length -= 1

    if substring_length == 0:
        print ('There is no common substring')
