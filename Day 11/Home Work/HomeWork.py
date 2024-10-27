correct_password = "goa1234"


attempts = 3

while attempts > 0:
    
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        
        attempts -= 1
        if attempts > 0:
            print(f"Try again. Attempts left: {attempts}")
        else:
            print("No attempts left. Access denied.")