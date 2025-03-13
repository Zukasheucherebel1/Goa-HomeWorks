def matrix_addition(a, b):
    for row in range(len(a)):
        for index in range(len(a)):
            a[row][index] += b[row][index]
    return a
def diamond(n):
    if n%2 == 0 or n < 0:
        return None
    
    result = ''
    for i in range(n):
        s = 0 #number of diamons
        k = 0 #number of spaces
        
        if i < n/2:
            k = i*2 + 1 
            s = (n - k) // 2 
        else:
            s = i - n//2
            k = n - 2 * s
        
        result += ' '*s + '*'*k +'\n'
        
    return result
