name = ['adi', 'sam','thief', 'aman', 'raj']

for n in name:
    if n == 'thief':
        print("theif found")
        break
    else:
        print(f"{n} is innocent")
else: 
    print("no theif found")

# for else is also a thing in python if the for loop do not break and fully execute then the else loop run