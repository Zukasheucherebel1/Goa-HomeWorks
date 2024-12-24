def check_exam(arr1,arr2):
    score = 0
    for i in range(0,4):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] == "" or arr2[i] == "":
            score += 0
        else: 
            score -= 1
    
    return score if score >= 0  else 0

from gmpy2 import next_prime, is_prime # type: ignore

def backwards_prime(start, stop):
    res = []
    i = start
    while i<= stop :
        i = next_prime(i)
        if is_prime(int(str(i)[::-1])) and i<=stop and int(str(i)[::-1])!=i: res.append(int(i))
    return res

def sum_dig_pow(a, b):
    result = []
    for n in range(a, b+1):
        digits = [int(i) for i in str(n)]
        dig_sum = sum([pow(d, i+1) for i, d in enumerate(digits)])
        if dig_sum == n: 
            result.append(n)
    return result