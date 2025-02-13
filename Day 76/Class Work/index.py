def find_missing(a):
    for i in range(len(a))[1:-1]:
        m = a[i] - a[i-1]
        n = a[i+1] - a[i]
        if m > n:
            return a[i-1] + n
        elif m < n:
            return a[i] + m
        

        