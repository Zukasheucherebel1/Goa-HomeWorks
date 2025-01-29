def high(x):
    
    sc_a ={}
    pos = 1
    for i in range(97,123):
        sc_a[chr(i)] = pos
        pos +=1
    
    words = []
    
    n = 0
    words.append("")
    for b in x:
        
        if b != " ":
            words[n] += b
        else:
            
            #new word
            words.append("")
            n +=1 
    
    w_n = 0
    sc_g = 0
    h_w = ""
    while len(words) > w_n:
        temp_sc = 0
        
        for j in words[w_n]:
            temp_sc += sc_a[j.lower()]
        
        if temp_sc > sc_g:
            sc_g = temp_sc
            h_w = words[w_n]
            
        w_n +=1
        
    return h_w
    



def even_fib(n):
    a = 0
    b = 1
    result = 0
    
    while a < n:
        if a % 2 == 0:
            result += a
        a, b = b, a+b
    return result



def array_diff(a, b):
    new_list = []
    for val in a:
        if val not in b:
            new_list.append(val)
            
    return new_list 

