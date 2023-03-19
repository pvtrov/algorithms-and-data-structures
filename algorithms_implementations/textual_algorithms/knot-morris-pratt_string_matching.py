# Returns how many times pattern appear in given text

def prefix_function(pattern):
    lps = [0] * len(pattern)
    l = 0
    i = 1

    while i < len(pattern):
        while l > 0 and pattern[i] != pattern[l]:
            l -= 1

        if pattern[i] == pattern[l]:
            l += 1

        lps[i] = l
        i += 1

    return lps


def kmp_string_matching(text, pattern):
    lps = prefix_function(pattern)
    result = []
    i = 0
    j = 0

    while i < len(text):
        if text[i] != pattern[j]:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
        else:
            i, j = i+1, j+1
            if j == len(pattern):
                result.append(i-j)
                j = lps[j-1]

    return len(result)
