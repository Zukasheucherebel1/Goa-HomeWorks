# ვკრავთ ციკლს 1-დან 50-მდე
for i in range(1, 51):
    # თუ რიცხვი იყოფა 4-ზე
    if i % 4 == 0:
        # ვაპრინტებთ რიცხვის კუბს
        print(i ** 3)


# ვქმნით ციკლს 1-დან 100-მდე
for i in range(1, 101):
    # თუ რიცხვი იყოფა 3-ზეც და 5-ზეც
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz {i}")
    # თუ რიცხვი მხოლოდ 3-ზე იყოფა
    elif i % 3 == 0:
        print(f"Fizz {i}")
    # თუ რიცხვი მხოლოდ 5-ზე იყოფა
    elif i % 5 == 0:
        print(f"Buzz {i}")


# ვპოულობთ 1-დან 20-მდე ყველა ლუწი რიცხვის ჯამს
even_sum = sum(i for i in range(1, 21) if i % 2 == 0)

# ვპოულობთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამს
odd_sum = sum(i for i in range(1, 21) if i % 2 != 0)

# ორივე ჯამს ვწევთ მე-5 ხარისხში
even_sum_5 = even_sum ** 5
odd_sum_5 = odd_sum ** 5

# ვადარებთ და ვბეჭდავთ იმ მნიშვნელობას, რომელიც მეტია
if even_sum_5 > odd_sum_5:
    print("Even sum to the power of 5 is greater:", even_sum_5)
else:
    print("Odd sum to the power of 5 is greater:", odd_sum_5)



result = True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5
print(result)  # შედეგი: True



# მომხმარებლისგან რიცხვის მიღება
number = int(input("Enter a number: "))

# მარტივი რიცხვის შემოწმების ფუნქცია
def is_prime(num):
    if num < 2:
        return False  # 1 და ნაკლები არ არის მარტივი რიცხვი
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # თუ გაყოფა შესაძლებელია, რიცხვი არ არის მარტივი
    return True

# შედეგის ბეჭდვა
if is_prime(number):
    print("Number is prime")
else:
    print("Number is not prime")




