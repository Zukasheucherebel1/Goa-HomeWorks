def past(h, m, s):
    m += h * 60
    s += m * 60
    ms = s * 1000
    return ms

def is_valid_IP(string):
    parts = string.split(".")
    if len(parts)!=4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        if len(item)>1 and item[0]=='0':
            return False
        i = int(item)
        if i <0 or i >255:
            return False
    return True