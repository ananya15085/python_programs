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

s = [50, 40, 70, 80, 90]
print(s)          
#[50, 40, 70, 80, 90]
fs = frozenset(s)
print(fs)
#frozenset({70, 40, 80, 50, 90})
fs = frozenset("abcdefg")
print(fs)
#frozenset({'a', 'e', 'g', 'd', 'c', 'f', 'b'})