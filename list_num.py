numbers = [1, 2, 314]
print(id(numbers))            #1974289348544
print(id(numbers[2]))         #2001416915024

numbers[2] = 3  # Mutation
print(id(numbers))            #2159092152256
print(id(numbers[2]))         #2794658248640

print(numbers)                #[1, 2, 3]




numbers = [2, 4, 3, 1]
last_added = numbers.append(5)
print(last_added)                #None
print(numbers)                   #[2, 4, 3, 1, 5]

sorted_numbers = numbers.sort()
print(sorted_numbers)            #None
print(numbers)                   #[1, 2, 3, 4, 5]




# Regular operator
numbers = [1, 2, 3] + [4, 5, 6]
print(numbers)
#[1, 2, 3, 4, 5, 6]

# Augmented operator
numbers = [1, 2, 3]
print(id(numbers))         #2075580783488
numbers += [4, 5, 6]
print(numbers)             #[1, 2, 3, 4, 5, 6]
print(id(numbers))         #2075580783488