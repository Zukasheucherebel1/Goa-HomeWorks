def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total


def number(stops):
    return sum(i - o for i, o in stops)

