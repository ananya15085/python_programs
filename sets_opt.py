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
#2279593003040

fruits |= {"banana"}  # Augmented union
print(fruits)
#{'orange', 'apple', 'banana'}
print(id(fruits))
#2279593003040

fruits = {"apple", "orange"}
print(id(fruits))
#2279593352480

fruits &= {"apple"}  # Augmented intersection
print(fruits)
#{'apple'}
print(id(fruits))