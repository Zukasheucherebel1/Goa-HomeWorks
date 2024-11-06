numbers = [3, 7, 12, 5, 25, 8]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("ყველაზე დიდი რიცხვი:", max_num)


import math

numbers = [3, 5, 6]
factorials = []
for num in numbers:
    factorials.append(math.factorial(num))
print("ფაქტორიალები:", factorials)



numbers = [3, 7, 12, 5, -2, 8]
min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
print("ყველაზე პატარა რიცხვი:", min_num)



numbers = [3, 7, 12, 5, -2, 8]
min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
print("ყველაზე პატარა რიცხვი:", min_num)



numbers = [3, -4, 12, -7, 5, -9, 8]
negatives = []
index = 0
while index < len(numbers):
    if numbers[index] < 0:
        negatives.append(numbers[index])
    index += 1
print("უარყოფითი რიცხვები:", negatives)



numbers = [3, 7, 12, 5, 25, 8]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])


chars = ['a', 'b', 'a', 'c', 'd', 'b', 'e']
unique_chars = []
for char in chars:
    if char not in unique_chars:
        unique_chars.append(char)
print("უნიკალური სიმბოლოები:", unique_chars)



year = int(input("შეიყვანეთ წელი: "))
century = (year - 1) // 100 + 1
print(f"{year} წელია {century}-ე საუკუნე")

