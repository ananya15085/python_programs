# Regular operators
fruits = {"apple", "orange"} | {"banana"}       # Union
print(fruits)
#{'banana', 'orange', 'apple'}

fruits = {"apple", "orange"} & {"apple"}       # Intersection
print(fruits)
#{'apple'}

fruits = {"apple", "orange"} - {"apple", "banana"}  # Difference
print(fruits)
#{'orange'}

fruits = {"apple", "orange"} ^ {"apple", "banana"}  # Symmetric difference
print(fruits)
#{'banana', 'orange'}

# Augmented operators
fruits = {"apple", "orange"}
print(id(fruits))
#1895090669600

fruits |= {"banana"}  # Augmented union
print(fruits)
#{'orange', 'apple', 'banana'}
print(id(fruits))
#1895090669600

fruits = {"apple", "orange"}
print(id(fruits))
#1895091019040

fruits &= {"apple"}  # Augmented intersection
print(fruits)
#{'apple'}
print(id(fruits))
#1895091019040