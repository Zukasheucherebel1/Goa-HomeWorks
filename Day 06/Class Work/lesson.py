
name = input("შეიყვანეთ თქვენი სახელი: ")  
surname = input("შეიყვანეთ თქვენი გვარი: ") 
age = input("შეიყვანეთ თქვენი ასაკი: ")  
email = input("შეიყვანეთ თქვენი იმეილი: ")  


print("\nთქვენი მონაცემები:")
print(f"სახელი: {name}")
print(f"გვარი: {surname}")
print(f"ასაკი: {age}")
print(f"იმეილი: {email}")


num1 = float(input("enter first number: "))  
num2 = float(input("enter second number: "))  

addition = num1 + num2 
subtraction = num1 - num2 
multiplication = num1 * num2  
division = num1 / num2 if num2 != 0 else "შეცდომა"

print("\nოპერაციების შედეგები:")
print(f"{num1} + {num2} = {addition}")  
print(f"{num1} - {num2} = {subtraction}")  
print(f"{num1} * {num2} = {multiplication}") 
print(f"{num1} / {num2} = {division}")  

# კომენტარები

# input() ფუნქცია გამოიყენება იმისთვის, რომ მომხმარებელმა შეიყვანოს მონაცემები პროგრამაში.
# მაგალითად, სახელი, გვარი, ასაკი და იმეილი.
# output() ფუნქცია ამ მონაცემებს ბეჭდავს ტერმინალში და აჩვენებს შედეგებს.
# ეს უზრუნველყოფს მომხმარებელს ზუსტი ინფორმაციის ნახვას და შესრულებული ოპერაციების შედეგების შემოწმებას.
