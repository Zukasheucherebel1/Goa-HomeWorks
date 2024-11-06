numbers = [3, 8, 15, 22, 5, 10, 12, 7, 6, 19]


sum_even = 0
sum_odd = 0


i = 0


while i < len(numbers):
    if numbers[i] % 2 == 0:  #ლუწი
        sum_even += numbers[i]
    else:  #კენტი
        sum_odd += numbers[i]
    i += 1

if sum_even > sum_odd:
    print("The sum of even numbers is greater:", sum_even)
elif sum_odd > sum_even:
    print("The sum of odd numbers is greater:", sum_odd)
else:
    print("Both sums are equal:", sum_even)






#სია
symbols = ['m', 'a', 'm', 'a', 's', 'h', 'e', 'n', 'i']

# ცვლადი სიმბოლოების კონკადინაციისთვის
result = ""

#თითოეული სიმბოლოს ჩამატება
for symbol in symbols:
    result += symbol

print(result)
