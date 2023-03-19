# Returns how many times pattern appear in given text

def transition(pattern):
    splitted = list(pattern)
    characters = set(pattern)

    result = []
    for q in range(len(pattern) + 1):
        result.append({})
        for a in characters:
            k = min(len(pattern), q+1)
            suffix = pattern[:q] + a
            while pattern[:k] != "" and pattern[:k] != suffix[q - k + 1:]:
                k -= 1
            result[q][a] = k
    return result


def finite_automaton_string_matching(text, pattern):
    delta = transition(pattern)
    q = 0
    result = []

    for s in range(0, len(text)):
        if text[s] in delta[q]:
            q = delta[q][text[s]]
            if q == len(delta) - 1:
                result.append(s + 1 - q)
        else:
            q = 0

    return len(result)