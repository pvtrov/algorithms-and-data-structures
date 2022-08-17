from egzP6atesty import runtests 


def put_into_buckets(buckets, passwords):
    for password in passwords:
        buckets[len(password)].append(password)


def sort_in(letters_number):
    max_ = -1
    right_bucket = []

    for tuple in letters_number:
        if tuple[0] > max_:
            max_ = tuple[0]

    buckets = [[] for _ in range(max_+1)]
    for tuple in letters_number:
        buckets[tuple[0]].append(tuple)

    for i in range(len(buckets)-1, -1, -1):
        for j in range(len(buckets[i])):
            right_bucket.append(buckets[i][j][1])

    return right_bucket


def count_letters_and_sort(bucket):
    letters_number = []

    for word in bucket:
        counter = 0
        for letter in word:
            if 97 <= ord(letter) <= 123:
                counter += 1
        letters_number.append((counter, word))

    return sort_in(letters_number)


def google(H, s):
    max_ = -1

    # O(n)
    for password in H:
        if len(password) > max_:
            max_ = len(password)

    buckets = [[] for _ in range(max_+1)]
    # O(n)
    put_into_buckets(buckets, H)

    new_buckets = []
    # O(nk)
    for bucket in buckets:
        if bucket:
            new_buckets.append(count_letters_and_sort(bucket))

    strong_pass = []
    for i in range(len(new_buckets)-1, -1, -1):
        if new_buckets[i]:
            strong_pass.extend(new_buckets[i])

    return strong_pass[s-1]


runtests ( google, all_tests=True )
# H = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
# s = 3
# print(google(H, s))
