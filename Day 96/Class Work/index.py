def simplify(number): 
   
    if number == 0:
        return ""
    
    str_n = str(number)
    length = len(str_n)
    
    result = []
    
    for i, digit in enumerate(str_n):
        if digit != "0":
            power = length - i - 1
            if power > 0:
                result.append(f"{digit}*{10 ** power}")
            else:
                result.append(digit)
                
    return "+".join(result)