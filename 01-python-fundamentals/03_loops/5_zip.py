cus = ['aditya', 'priya', 'riya', 'isha']
amount = [100, 20 ,40]
num  = [1,2,3,4]
list = ['a','b','c','d','e','f','g']

for name , amount , serial, letter in zip(cus,amount,num,list):
    print(f"{serial} , {letter} : {name} paid {amount}")

# zip is used in to access same index of each  array ,it will only go to the minimum length of the iterables
# you can zip as must iterables you want