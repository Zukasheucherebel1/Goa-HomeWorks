words = ["apple", "banana", "cherry"]
for word in words:
    print(len(word))



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = 0
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        sum_even += numbers[i]
    i += 1
print(sum_even)


names = ["Alice", "Bob", "Anna", "Charlie", "Amanda"]
for name in names:
    if name.startswith("A"):
        print(name)


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_sum = sum(num for num in numbers if numbers.count(num) == 1)
print(unique_sum)



elements = [10, 20, 30, 40, 50]
print(elements[2:4])


text = "Hello, World!"
print(text[-3:])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:])
