words = ['a','s','g']
awords = ['w','e','r']

words.append('f')
print(f"{words}")
print(f"{awords}")

awords.insert(2,'t')
words.remove('g')

words.extend(awords)
print(f"{words}")

words.reverse()
print(f"{words}")

words.sort()
print(f"{words}")

print(f"{max(words)}")
print(f"{min(words)}")

# we can perform many operations on tuples like append, insert, remove, extend, sort, reverse

str = bytearray(b"Aditya")
print(f"{str[2]}")
str.replace(b"Adi" , b"Tha") # will not work we have to reassign 
print(f"{str}")
str = str.replace(b"Adi" , b"Tha") 
print(f"{str}")

# we can use arithmatic operation on lists too
word = words + awords
print(f"{word * 3}") #also maintain the order