  #program to add two complex numbers
c1 = 2.5+2.5j
c2 = 3.0-0.5j
c3 = c1+c2
print("sum=" , c3)
#sum= (5.5+2j)


#convert the datatypes explicity
x = 15.56
print(int(x))            #15

num = 15
print(float(num))        #15.0

n = 10
print(complex(n))        #(10+0j)

a = 10
b = -5
print(complex(a,b))      #(10-5j)

a = 5
b = 2
print(complex(a,b))      #(5+2j)

#program to convert into decimal number system
n1 = 0o17
n2 = 0b111001
n3 = 0x1c2

n = int(n1)
print('octal 17=' ,n)             #octal 17= 15
n = int(n2)
print('binary 1110010 =',n)       #binary 1110010 = 114
n = int(n3)
print('hexadecimal 1c2 =',n)      #hexadecimal 1c2 = 450

str = "1c2"
n = int (str,16)
print(n)                          #450

str = "0b1"
n = int (str,2)
print(n)
