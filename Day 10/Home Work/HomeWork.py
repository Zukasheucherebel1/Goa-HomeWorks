num = int(input("Enter a number: "))
print(f"{num} The number is included in 100 {100 // num}.")





i = 1
sum_odd = 0

while i <= 20:
    if i % 2 != 0:
        sum_odd += i
    i += 1

print(f"is the sum of odd numbers from 1 to 20: {sum_odd}")



num1 = int(input("enter I number: "))
num2 = int(input("enter II number: "))

if num1 > num2:
    print(f"There are more numbers: {num1}")
elif num2 > num1:
    print(f"There are more numbers: {num2}")
else:
    print("Both numbers are equal")




num = int(input("enter number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}-of factorial is: {factorial}")




num = int(input("enter number: "))
square_sum = 0

for i in range(1, num + 1):
    square_sum += i ** 2

print(f"{num}-is the sum of the squares of the numbers up to: {square_sum}")



import random

target = random.randint(1, 20) 
guess = None

while guess != target:
    guess = int(input("Guess the number from 1 to 20: "))
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("You win")
