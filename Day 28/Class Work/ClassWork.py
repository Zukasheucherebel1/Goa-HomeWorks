8 kyu
https://www.codewars.com/kata/551b4501ac0447318f0009cd
def boolean_to_string(b):
    return str(b)

https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def findSmallestInt(arr):
    return min(arr)



7 kyu
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
def solution(text, ending):
    len_end = len(ending)
    word = text[-len_end:]
    if word == ending:
        print('true')
        return True
    else:
        print('false')
        return False
https://www.codewars.com/kata/5412509bd436bd33920011bc
def maskify(cc):
    newstring = ''
    for character in cc[0:-4]:
        newstring += '#'
    for number in cc[-4:]:
        newstring += number
    return newstring


6 kyu
https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

level 47
არ გვქონდა საკლასო დავალება, რადგან გაკვეთილი დაეთმო თეორიულ მასალას