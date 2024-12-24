def most_frequent_item_count(collection):
    count = 0
    for i in set(collection):
        tempcount = collection.count(i) 
        if tempcount > count: 
            count = tempcount
    return count
    


    def move_ten(st):
    
    res = ""
    
    for i in st:
        
        val = ord(i) +10
        if val > 122:
            res += chr(val - 26)
        else:
            res += chr(val)
        
    return res


def collatz(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
            count += 1
        else:
            n = n * 3 + 1
            count += 1
    return count
