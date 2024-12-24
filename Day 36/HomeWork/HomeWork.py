def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

def number(stops):
    return sum(i - o for i, o in stops)


def digital_root(n):
	return n%9 or n and 9

def spin_words(sentence):
    return " ".join(x[::-1] if len(x) >= 5 else x for x in sentence.split())


