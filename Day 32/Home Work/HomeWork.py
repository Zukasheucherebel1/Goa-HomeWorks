def smash(words):
    
    i=0
    l=len(words)
    str1=""
    while i<l:
        if i<l-1:
            str1+=words[i] + " "
        else: 
            str1+=words[i]
        i+=1
        
    return str1

def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high

def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output

def max_min_avg(arr):
    return [max(arr), min(arr), sum(arr)/len(arr)]

def sum_of_squares(arr):
    sum = 0
    for i in arr:
        sum += i**2
    return sum