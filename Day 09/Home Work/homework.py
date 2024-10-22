summa = 0
number = 1

# while ციკლი
while number <= 50:
    summa += number  
    number += 1      


    # სწორი PIN კოდი
correct_pin = "1234"


while True:
    user_pin = input("Please enter a 4-digit PIN code: ")
    
    if user_pin == correct_pin:
        print("CORRECT PIN!")
        break  
    else:
    
        print("wrong PIN.")



        # სასურველი რიცხვი, რომელიც უნდა გამოიცნოს მომხმარებელმა
secret_number = 7  


guess = None  


while guess != secret_number:
  
    guess = int(input("Guess the number from 1 to 10: "))

    
    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10!")
    elif guess < secret_number:
        print("Try a larger number!")
    elif guess > secret_number:
        print("Try a smaller number!")


print("Congratulations! Guess the correct number!")




