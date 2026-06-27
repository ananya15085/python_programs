s ={10, 20, 30, 20, 50}
print(s)
#{10, 20, 50, 30}

ch = set("Hello")
print(ch)
#{'e', 'l', 'H', 'o'}

lst = [1, 2, 5, 4, 3]
s = set(lst)
print(s)
#{1, 2, 3, 4, 5}

s = {1, 2, 3, 4, 5}
print(s[0])           #1
print(s[0:2])         #(1, 2)
s = {1, 2, 3, 4, 5}
s.update([50,80])
print(s) 
s.remove([50])
print(s)