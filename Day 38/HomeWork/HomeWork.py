def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for number in range(a, b+1):
        digits = [int(i) for i in str(number)]
        s = 0
        for idx, val in enumerate(digits):
            s += val ** (idx + 1)
        if s == number:
            res.append(number)
    return res


def max_multiple(divisor, bound):
    l = []
    for int in range(bound + 1):
        if int % divisor == 0:
            l.append(int)
    return max(l)

def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
