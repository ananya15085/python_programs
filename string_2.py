greeting = "Hello!"
print(id(greeting))        #2049090472576

greeting = "Hello, World!"
print(id(greeting))         #2049090453104

str = "welcome"
str = 'welcome'
str1 = "This is a book on python which discusses all the topics of core python."
str2 = 'This is a book on python which discusses all the topics of core python.'

str = """ This is a 'core python' book."""
print(str)
#This is a 'core python' book.

str = '''This is a "core python" book.'''
print(str)
#This is a "core python" book.

s = 'Welcome to Core Python'
print(s)
#Welcome to Core Python

print(s[0])          #W
print(s[3:7])        #come
print(s[11:])        #Core Python
print(s[-1])         #n
print(s*2)