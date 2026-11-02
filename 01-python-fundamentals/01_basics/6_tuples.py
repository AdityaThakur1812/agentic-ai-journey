tup = ("aditya", "thakur", "priya" , "riya") # once it is defined we cn not add or remove values from it
(str1,str2,str3,st4) = tup #variable for each element in the tuple remember the size should be equal

print(f"{str1}")
print(f"{str2}")
print(f"{str3}")
print(f"{st4}")

a,b = 2,1 # this is the ability of tuple
print(f"{a}")
print(f"{id(a)}")
print(f"{b}")
print(f"{id(b)}")
a,b = b,a
print(f"{a}")
print(f"{id(a)}")
print(f"{b}")
print(f"{id(b)}")
print(f"{tup[0]}")

#number is immutable so the reference swapped not the value

print(f"is aditya present : {'aditya' in tup}") #case sensitive , use in keyword to find specific element in the tuple