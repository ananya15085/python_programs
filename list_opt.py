# Regular operator
letters = ["A", "B", "C"] * 3
print(letters)
#['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']]

# Augmented operator
letters = ["A", "B", "C"]
print(id(letters))              #2234172922752
letters *= 3
print(letters)
#['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
print(id(letters))               #2599970626432