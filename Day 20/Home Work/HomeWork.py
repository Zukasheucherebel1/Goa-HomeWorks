
def greet(name):
    print(f"Hello {name}")


greet("Nika")
greet("gocha")



def multiply(a, b):
    print(a * b)

# Call the multiply function
multiply(4, 5)



def print_reverse(lst):
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end=" ")
    print()  # For new line


print_reverse([1, 2, 3, 4, 5])


def filter_greater_than_10(lst):
    result = []
    for num in lst:
        if num > 10:
            result.append(num)
    return result


print(filter_greater_than_10([5, 15, 8, 12, 3, 20]))



def trim_list(lst):
    return lst[1:-1]

# Call the trim_list function
print(trim_list([1, 2, 3, 4, 5]))



def product_of_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return sum1 * sum2

# Call the product_of_sums function
print(product_of_sums([1, 2, 3], [4, 5, 6]))



def find_duplicates(lst):
    duplicates = []
    i = 0
    seen = set()
    while i < len(lst):
        if lst[i] in seen and lst[i] not in duplicates:
            duplicates.append(lst[i])
        else:
            seen.add(lst[i])
        i += 1
    return duplicates

# Call the find_duplicates function
print(find_duplicates([1, 2, 3, 2, 4, 3, 5, 6, 4]))



def get_even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

# Call the get_even_numbers function
print(get_even_numbers([1, 2, 3, 4, 5, 6]))



def names_starting_with_n(names):
    n_names = []
    for name in names:
        if name.startswith("N"):
            n_names.append(name)
    return n_names

# Call the names_starting_with_n function
print(names_starting_with_n(["lolo", "mari", "Nia", "tako", "kacho"]))
