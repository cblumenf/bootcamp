def longest_common_substring(s1, s2):
    """Return one of the longest common substrings"""

    # Make sure s1 is the shorter
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # Start with the entire sequence and shorten
    substr_len = len(s1)
    while substr_len > 0:
        # Try all substrings
        for i in range(len(s1) - substr_len + 1):
            if s1[i:i+substr_len] in s2:
                return s1[i:i+substr_len]

        substr_len -= 1

    # If we haven't returned, there is no common substring
    return ''
