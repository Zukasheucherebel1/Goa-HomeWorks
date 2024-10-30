
items = []


for i in range(5):
    element = input(f"Input the {i+1}-th element: ")
    items.append(element)


print("your list:", items)






fruits = ["Apple", "Banana", "Orange"]


favorite_fruit = input("Bring your favorite fruit: ")


if len(fruits) % 2 == 0:
    fruits.append(favorite_fruit)
    print("updated list:", fruits)
else:
    print("Fruit was not added to the list because the last index is not even.")




names = ["mari", "gio", "nika"]


user_name = input("enter your name: ")


if len(user_name) >= 5:
    names.append(user_name)
    print("updated list:", names)
else:
    print("Name is too short.")



fruits = ["Apple", "Banana", "Orange"]
print(fruits[0])  # გამოიტანს 'ვაშლი'
print(fruits[2])  # გამოიტანს 'ფორთოხალი'
