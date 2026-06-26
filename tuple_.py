letters = ("a", "b", "c", "d")
print(type(letters))
#<class 'tuple'>

print (letters[0])         #a
print (letters[1])         #b
print (letters[2])         #c

(letters[0])= "A"
print((letters[0]))        #TypeError: 'tuple' object does not support item assignment