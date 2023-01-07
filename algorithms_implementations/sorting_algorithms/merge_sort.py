# MergeSort

def merge(tab1, tab2):  # scalanie posortowanych tablic
    len1 = len(tab1)
    len2 = len(tab2)
    length = len1 + len2
    new_tab = [0] * length
    t1, t2 = 0, 0
    for i in range(length):
        if t1 < len1 and t2 < len2:
            if tab1[t1] > tab2[t2]:
                new_tab[i] = tab2[t2]
                t2 += 1
            else:
                new_tab[i] = tab1[t1]
                t1 += 1
        elif t1 < len1:
            new_tab[i] = tab1[t1]
            t1 += 1
        else:
            new_tab[i] = tab2[t2]
            t2 += 1
    return new_tab


def mergesort(Tab):  # algo mergesorta  T(n) = O(nlogn)
    if len(Tab) < 2:
        return Tab

    c = len(Tab) // 2
    T1 = mergesort(Tab[0:c])
    T2 = mergesort(Tab[c:])

    return merge(T1, T2)
