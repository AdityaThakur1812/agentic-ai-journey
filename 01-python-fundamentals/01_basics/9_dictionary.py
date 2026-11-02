hey = dict()
hey = {"name": "aditya", "last": "thakur", "age": 22}
hey["height"] = 5.11
print(f"{hey}")

print(f"{hey.pop('last')}")

print(f"{hey}")

print(f"{hey.keys()}")
print(f"{hey.values()}")
print(f"{hey.items()}")
print(f"{hey.popitem()}")

# we can also use'in' 
# the difference between pop and popitem is , in pop you can remove any item with the help of key 
# and popitem only remove the last added item

mor = dict(weight = 66, gender = "Male") 

hey.update(mor)# it simply append the dictionary
print(f"{hey}")

# we can use get to handle error if we want to retrieve the value of a undefined or unavailable key
# age = hey['nu'] it will give error

age = hey.get("nu",'age') # if nu not available we get the age string not the age value
print(f"{age}")
age = hey.get('age',"nu") 
print(f"{age}")