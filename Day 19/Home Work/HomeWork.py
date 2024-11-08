
items = ["apple", "banana", "cherry", "date", "elderberry"]
items = items[:-2]  
print(items)


my_string = "Hello, world!"
print(my_string[::-1])


numbers = [10, 23, 5, 67, 12, 78, 34, 89, 2, 45]
smallest = min(numbers)
largest = max(numbers)
sum_of_smallest_and_largest = smallest + largest
print(sum_of_smallest_and_largest)




def is_palindrome(s):
    return s == s[::-1]

my_string = "madam"
print("Is palindrome:", is_palindrome(my_string))

numbers = [10, 23, 5, 67, 12, 78, 34, 89, 2, 45]
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)



original_list = [1, 0, 1, 1, 0, 0, 1]
new_list = []


for value in original_list:
    if value == 1:
        new_list.append(True)
    else:
        new_list.append(False)


print(new_list)

