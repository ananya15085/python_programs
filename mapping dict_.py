d = {10: 'kamal', 11: 'pranav', 12: 'hasini', 13: 'arun', 14:'ritu'}
print(d)
#{10: 'kamal', 11: 'pranav', 12: 'hasini', 13: 'arun', 14: 'ritu'}
print(d[10])    #kamal
print(d[12])    #hasini
print(d.keys())
#dict_keys([10, 11, 12, 13, 14])
print(d.values())
#dict_values(['kamal', 'pranav', 'hasini', 'arun', 'ritu'])
d[10] = 'raman'
print(d)
#{10: 'raman', 11: 'pranav', 12: 'hasini', 13: 'arun', 14: 'ritu'}
del(d[11])
print(d)
#{10: 'raman', 12: 'hasini', 13: 'arun', 14: 'ritu'}
     