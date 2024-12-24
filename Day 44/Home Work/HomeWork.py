def dup(arry):
    array_new = []
    for string in arry:
        string_new = ""
        prev = None
        for char in string:
            if char != prev:
                string_new += char
            prev = char
        array_new.append(string_new)
        
    return array_new

    
    def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)