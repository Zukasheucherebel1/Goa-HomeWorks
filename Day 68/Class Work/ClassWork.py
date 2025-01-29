def friend(x):
    friendsNames = [] 
    for friendName in x: 
        if len(friendName) == 4: 
            friendsNames.append(friendName)
    return friendsNames


def remove_url_anchor(url): 
    s = ""
    for letter in url:
        if letter != "#":
            s += letter
        else:
            return s
    return url


def capitals(word):
    arr = []
    for idx, c in enumerate(word):
    	if ord(c) < 96:
        	arr.append(idx)
    return arr


def sum_digits(number):
    num = list(str(number))
    total = 0 
    if num[0] == "-":
        num = num[1:]
    for i in num:
        
        total += int(i)
    
    return total


def sum_digits(n):
    res = 0
    n = abs(n)
    while n:
        res += n % 10
        n //= 10
    return res



def smash(words):
    result = ""
    for word in words:
        if len(words) == 0:
            result = ""
        elif len(words) == 1:
            result = str(words[0])
        else:
            result += f"{word} "
    if len(result)>0:
        if result[-1] == " ":
            result = result[:-1]
    return result



def count_smileys(arr):
    
    counter = 0
    
    for char in arr:
        
        if char[0] == ":" or char[0] == ";" :
            
            if char[1] == ")" or char[1] == "D" :
                counter +=1
            
            if len(char) > 2:
                
                if char[1] == "-" or char[1] == "~" :
                    
                    if char[2] == ")" or char[2] == "D" :
                        counter +=1
                    
    return counter





def pyramid(n):
    
    if n == 0:
        return []
    
    ans = []
    for x in range(1,n+1):
        ans.append([1]*x)
        
    return ans




def shortest_steps_to_num(num):
    k = 0
    while num > 1:
        if num % 2:
            num -= 1
        else:
            num //= 2
        k += 1
    return k