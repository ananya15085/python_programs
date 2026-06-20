a = 10
b = bin(a)
print(b)                  #0b1010
b = oct(a)
print(b)                  #0o12
b = hex(a)
print(b)                  #0xa

n = 25
print(bin(n))              #0b11001
print(oct(n))              #0o31
print(hex(n))              #0x19

n = 50
print(bin(n))              #0b110010
print(oct(n))              #0o62
print(hex(n))              #0x32

n = 64
print(bin(n))              #0b1000000
print(oct(n))              #0o100
print(hex(n))              #0x40

n = 255
print(bin(n))              #0b11111111
print(oct(n))              #0o377
print(hex(n))              #0xff

print(int('1a',16))         #26
print(int('1010',2))        #10
print(int('12',8))          #10
print(int('100',8))         #64
print(int('77',8))          #63
print(int('ff', 16))        #255



