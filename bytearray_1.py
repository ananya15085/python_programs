greeting = "Hello!"
mutable_greeting = bytearray(greeting.encode("utf-8"))
print(id(mutable_greeting))
#2770067455536

mutable_greeting[1] = ord("E")
print(mutable_greeting)
#bytearray(b'HEllo!')
print(id(mutable_greeting))