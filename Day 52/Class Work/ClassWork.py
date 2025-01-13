
def validPhoneNumber(phoneNumber):#-
    number = ''#-
    template = '(xxx) xxx-xxxx'#-
    for l in phoneNumber:#-
        if l.isdigit():#-
            number += 'x'#-
        else:#-
            number += l#-
#-
    return number == template#-
#-
#-
    def clean_string(string):#-
     def clean_string(string):#+
       out = ''
    for x in string:
        if x != '#': out += x#-
        else: out = out[:-1]#-
        if x != '#':#+
            out += x#+
        else:#+
            out = out[:-1]#+
    return out


def clean_string(string):
    out = ''
    for x in string:
        if x != '#': out += x
        else: out = out[:-1] 
    return out

def highest_rank(arr):
    best = 0
    occs = 0
    for item in arr:
        times = arr.count(item)
        if times > occs:
            best = item
            occs = times
        elif times == occs:
            if best < item:
                best = item
    return best