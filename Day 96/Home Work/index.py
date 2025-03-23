from collections import Counter

def find_arr(arrA, arrB, rng, wanted):
    ca, cb = Counter(arrA), Counter(arrB)
    m, n = rng
    m += (m % 2 == 1) == (wanted == 'even')
    r = range(m, n+1, 2)
    return [v for v in r if ca[v] > 1 and cb[v] > 1]