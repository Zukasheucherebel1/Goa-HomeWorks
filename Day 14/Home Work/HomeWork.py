
even_numbers = []
for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)
print("Even numbers from 1 to 100:", even_numbers)


numbers = list(range(1, 51))
for number in numbers[:]:
    if number % 2 != 0:
        numbers.remove(number)
print("After removing the odd numbers:", numbers)


fruits = ["ვაშლი", "ბანანი", "ატამი", "კივი", "მანგო", "სტაფილო", "გრეიფრუტი", "ყურძენი", "ანანასი", "ნეკერჩხალი"]
while len(fruits) > 2:
    fruits.pop()
    print("current list:", fruits)


numbers = [1, 2, 0, 1, 32, 1, 30, 1, 1, 21, 1, 1, 1]
count_of_ones = 0
for num in numbers:
    if num == 1:
        count_of_ones += 1
print("number 1 in the list", count_of_ones, "times")


short_words = []
long_words = []
for _ in range(5):
    word = input("Enter the word: ")
    if len(word) <= 5:
        short_words.append(word)
    else:
        long_words.append(word)
print("first list (<=5 characters):", short_words)
print("second list (>5 characters):", long_words)
