str = "Aditya is a good person "

print(f"{str}")
print(f"{str[0:2]}") # exclude 2
print(f"{str[0:]}")
print(f"{str[:2]}")
print(f"{str[0::4]}")

# we can encode and decode string

str1 = "Aditya Thakur"
str2 = str1.encode("utf-8")
print(f"{str2}")
str3 = str2.decode("utf-8")
print(f"{str3}")