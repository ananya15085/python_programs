greeting_str = "Hello, World!"
print(type(greeting_str))
#<class 'str'>

greeting_bytes = b"Hello, World!"
print(type(greeting_bytes))
#<class 'bytes'>



print (bytes("Español".encode("utf-8")))
#b'Espa\xc3\xb1ol'