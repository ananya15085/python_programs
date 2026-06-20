# create a list of byte numbers 
elements = [10, 20, 0, 40, 15]

#convert  the list into bytearray type array
x = bytearray(elements)
print(x[0])             #10

#modify the first two elements of x
x[0] = 88
x[1] = 99

for i in x:print(i)