greeting = "Hello, Pythonistas!"
print(greeting)           #Hello, Pythonistas!
print(id(greeting))        #2043651947504

greeting = greeting.upper()
print(greeting)            #HELLO, PYTHONISTAS!
print(id(greeting))        #2043651948016

greeting = greeting.lower()
print(greeting)            #hello, pythonistas!
print(id(greeting))        #2017678130608

greeting = greeting.title()
print(greeting)            #Hello, Pythonistas!
print(id(greeting))        #2017678130672