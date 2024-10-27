# მომხმარებლისგან ორი რიცხვის მიღება
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# რიცხვების მე-3 ხარისხში აყვანა და ჯამის გამოთვლა
sum_of_cubes = num1**3 + num2**3

# შედეგის ლუწი/კენტიობის შემოწმება
if sum_of_cubes % 2 == 0:
    print("Result is Even")
else:
    print("Result is Odd") 

