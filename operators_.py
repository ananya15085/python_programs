#ARITHMETIC OPERATORS
print(13+5)       #18
print(13-5)       #8
print(13*5)       #65
print(13/5)       #2.6
print(13%5)       #3
print(13**5)      #371293
print(13//5)      #2
d = (1+2)*3**2//2+3
print(d)           #16

#ASSIGNMENT OPERATORS
a = b = 1
print(a,b)      #1 1
a = 1 ; b = 2
print(a,b)      #1 2 
a,b = 1, 2
print(a,b)      #1 2

#UNARY MINUS
n = 10
print(-n)     #-10

num = -20
num = -num
print(num)    #20

#RELATIONAL OPERATORS
a = 1; b = 2
if (a>b):
    print("yes")
else:
    print("no")
#no

x = 15
print(10<x<20)    #True
print(10>=x<20)   #False
print(10<x>20)    #False
print(1<2<3<4)    #True
print(1<2>3<4)    #False
print(4>3<2>1)    #False
print(4>2>=2>1)   #True

#LOGICAL OPERATORS
x = 100
y = 200
print(x and y)     #200
print(x or y)      #100
print(not x)       #False

x = 1; y = 2; z = 3
if (x<y and y<z):
    print('yes')
else: 
    print('no')
#yes
x = 1; y = 2; z = 3
if (x>y and y<z):
    print('yes')
else: 
    print('no')
#no

#BOOLEAN OPERATORS
a = True
b = False 
print(a and a)    #True
print(a or a)     #true
print(b or b)     #False
print(b and b)    #False
print(a or b)     #True
print(a and b)    #False
print(not a)      #False
print(not b)      #True

#MEMBERSHIP OPERATORS
names =["rani", "yamini", "surekha", "veena"]
for name in names: 
    print(name)
#rani
#yamini
#surekha
#veena

postal = {'delhi':110001, 'mumbai':600001, 'kolkata':700001, 'chennai':5600001}
for city in postal:
    print(city, postal[city])
#delhi 110001
#mumbai 600001
#kolkata 700001
#chennai 5600001

#IDENTITY OPERATORS
a = 25
b = 25
print(id(a))     #140711990511480
print(id(b))     #140711990511480

a = 25
a = 25
if(a is b):
    print("a and b have same identity")
else:
    print("a and b do not have a same identity")
#a and b have same identity

one = [1,2,3,4]
two = [1,2,4,5]
if(one is two):
    print("one and two are same")
else:
    print("one and two are not same")
#one and two are not same
print(id("one"))    #1561084718432
print(id("two"))    #1561084718528

if(one == two):
  print("one and two are same")
else:
    print("one and two are not same")
