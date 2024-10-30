
friends = ["ზაკა", "შიო", "გიო", "სპარტაკა"]


print("best friend:", friends[0])


print("friend list:", friends)


friends[3] = "გოჩა"


print("updated list:", friends)


print("list lenght:", len(friends))







cars = ["BMW", "Audi", "Mercedes"]


def add_car(car_list, new_car):
    car_list.append(new_car)


add_car(cars, "Toyota")


print(" car list:", cars)







numbers = [10, 20, 30, 40, 50]


numbers[0] = 50


sum_first_last = numbers[0] + numbers[-1]


print("The sum of the first and last number:", sum_first_last)

