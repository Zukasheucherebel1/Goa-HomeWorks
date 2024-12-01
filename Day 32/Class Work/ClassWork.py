def manual_count(string, element):
    count = 0  
    for char in string:  
        if char == element:  
            count += 1  
    return count  



def manual_replace(string):
    result = ""  
    for char in string: 
        if char == " ":  
            result += "-"  
        else:
            result += char  
    return result  