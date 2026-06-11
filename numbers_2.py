word_counter = letter_counter = 0
print(id(word_counter))     #140722406540376
print(id(letter_counter))   #140722406540376

word_counter += 1
print(word_counter)           #1
print(id(word_counter))       #140722406540408
print(letter_counter)          #0
print(id(letter_counter))