tuple = (10, -20, 15.5, 'vijay', 'mary')
print(tuple)
#(10, -20, 15.5, 'vijay', 'mary')
print(tuple[0])        #10
print(tuple[1:4])      #(-20, 15.5, 'vijay')
print(tuple[-3])       #15.5
print(tuple[-1])       #mary
print(tuple*3)         
#(10, -20, 15.5, 'vijay', 'mary', 10, -20, 15.5, 'vijay', 'mary', 10, -20, 15.5, 'vijay', 'mary')

(tuple[0])=99
print(tuple[0])
#Traceback (most recent call last):
#TypeError: 'tuple' object does not support item assignment