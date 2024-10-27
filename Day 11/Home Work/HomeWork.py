count = 0
for i in range(1, 51):
    if i % 2 == 0:
        count += 1
print("ლუწი რიცხვების რაოდენობა 1-დან 50-მდე არის:", count)



sum_even = 0
count_even = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    i += 1

average = sum_even / count_even
print("ლუწი რიცხვების საშუალო არითმეტიკული 1-დან 100-მდე არის:", average)




i = 1
while i <= 30:
    if i % 3 == 0:
        print(i)
    i += 1



num = int(input("შეიყვანეთ რიცხვი: "))

print(f"{num}-ის ყველა გამყოფი:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)



num = int(input("შეიყვანეთ რიცხვი: "))

if num > 0:
    print("რიცხვი დადებითია")
elif num < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი არის 0")



year = int(input("შეიყვანეთ წელი: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} წელი არის ნაკიანი")
else:
    print(f"{year} წელი არ არის ნაკიანი")





score = int(input("შეიყვანეთ ქულა (1-დან 100-ის ჩათვლით): "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")




