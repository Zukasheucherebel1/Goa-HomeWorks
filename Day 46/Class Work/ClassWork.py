
def it(n):
    for i in range(1, n+1):
        yield from map(int, str(i))

def compute_sum(n):
    return sum(it(n))

    def sum_arrays(array1,array2):
    if array1 == [] and array2 == []:
        return []
    if array1 == []:
        return array2
    if array2 == [] or array2 == [0]:
        return array1
    a = list(map(str, array1))
    a= "".join(a)
    a = a.lstrip("0") or "0"
    print(a)

    b= list(map(str, array2))
    b = "".join(b)
    b = b.lstrip("0") or "0"
    print(b)
    if int(b) > 0:
        c = a + "+" + b
    else:
        c = a + b
    print(c)

    d = eval(c)
    print(d)
    d = list(str(d))
    print(d)
    if d[0] == "-":
        d =d[1:]
        d = list(map(int,d))
        d[0] = -abs(d[0])
    print(d)
    d = list(map(int,d))
    return d