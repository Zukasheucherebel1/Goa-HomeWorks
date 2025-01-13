def even_fib(m):
    a,b,s=0,1,0
    while a<m:
        if a%2==0:s+=a
        a,b=b,a+b
    return s

def two_oldest_ages(ages):
        l = []
        for i in ages:
            if len(l)<2:l.append(i)
            elif len(l)==2:
                if l[0]>l[1]: l=l[::-1]
                if i>l[1]: l.append(i);l=l[1:]
                elif i>l[0]: l.pop(0);l.append(i);l=l[::-1] 
        return [l,l[::-1]][l[0]>l[1]]


def sum_of_minimums(numbers):
    
    answer = []
    
    for array in numbers:
        answer.append(min(array))
        
    return sum(answer)



def gimme(input_array):
  
    for e in input_array:
        i = 0
        for p in range(len(input_array)):
            if e > input_array[p]:
                i+=1
            if e < input_array[p]:
                i-=1
        if i == 0:  
            for ele in range(len(input_array)):
                if e == input_array[ele]:
                    return ele
