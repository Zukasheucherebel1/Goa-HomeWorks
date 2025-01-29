

def prime_factors (n):
  # your code goes here
    res = []
    div = 2
    while n > 1:
        if n%div == 0:
            res.append(div)
            n //= div
        else:
            div += 1
    return res


def more_zeros(s):
    seen, res = set(), []
    
    for char in s:
        if char not in seen:
            b = bin(ord(char))[2:]
            if b.count('0') > len(b) / 2:
                res.append(char)
        seen.add(char)
        
    return res

def arrays_similar(seq1, seq2):
    if len(seq1) != len(seq2):
        return False
    count = 0
    for elem in seq1:
        if seq1.count(elem) == seq2.count(elem):
            count += 1
    if count == len(seq1):
        return True
    else:
        return False