fruits = frozenset(["apple", "orange", "banana"])

print(dir(fruits))

['difference',
'intersection',
'isdisjoint',
'issubset',
'issuperset',
'symmetric_difference',
'union'
] 

s = [50, 60, 70, 80, 90]
print(s)          
#[50, 60, 70, 80, 90]
fs = frozenset(s)
print(fs)
#frozenset({70, 80, 50, 90, 60})
fs = frozenset("abcdefg")
print(fs)
#frozenset({'f', 'd', 'b', 'c', 'a', 'e', 'g'})