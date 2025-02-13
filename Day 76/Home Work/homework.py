def solve(s):
    max_score = score = 0
    for char in s:
        if char in 'aeiou':
            score = 0
            continue
        score += ord(char) - ord('a') + 1
        if score > max_score:
            max_score = score
    return max_score

def filter_string(string):
    rez = ""
    for i in string:
        if i>='0' and i<='9':
            rez = rez + i
    return int(rez)

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