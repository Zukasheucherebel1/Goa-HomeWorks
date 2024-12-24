def validPhoneNumber(phoneNumber):
    number = ''
    template = '(xxx) xxx-xxxx'
    for l in phoneNumber:
        if l.isdigit():
            number += 'x'
        else:
            number += l
    
    return number == template

def longest_palindrome(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            sub = s[j:j+i]
            if sub == sub[::-1]:
                return i
    return 0

def max_sum_subarray(arr): 
    
    max_so_far = arr[0]
    curr_max = arr[0]   - max_so_far
    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far



def is_int_array(arr):
    try:
        return list(map(int, arr)) == arr
    except:
        return False
    

    