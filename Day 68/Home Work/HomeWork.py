def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
        

        import math

def largest_pair_sum(numbers):
    a, b = -math.inf, -math.inf
    for n in numbers:
        if n > a:
            if a > b:
                b = a
            a = n
        elif n > b:
            b = n
    return a + b