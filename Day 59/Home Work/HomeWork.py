def mineLocation(field):
    for i in range(len(field)):
        for y in range(len(field[i])):
            if field[i][y]==1:
                return [i,y]
            
            def compute_sum(n): 
                sum = 0
    for x in range(n+1):
        if x < 10:
            sum += x
        else:
            for n in str(x):
                sum += int(n)
    return sum

