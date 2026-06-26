greeting = "Hello!"
print(greeting[0])        #H
print(greeting[1])        #e

print(id(greeting[0]))        #140722406605896
print(id(greeting[1]))        #140722406607288

print(id(greeting))            #1847737600640
 
print(id(greeting['E']))           
#Traceback (most recent call last):
#typeError: name 'E' is not defined
  