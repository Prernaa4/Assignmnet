def remove_odd(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:   # even check
            new_list.append(n)
    return new_list

# Main program
my_list = [1, 2, 3, 4, 5, 6]
result = remove_odd(my_list)

print("Original list:", my_list)
print("New list:", result)