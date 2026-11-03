#walrus operator is a totally optional operator
#It makes the code little shorter 

num =13

if rem := num % 5:
    print("not divisible")

size = ['large' ,'small' , 'medium']

if (s := input("Please choose size").lower()) not in size:
    print(f"{s} size is not available")
else:
    print(f"You choose {s}")

flavor = ['chocolate', 'vanilla', 'butterscotch' , 'strawberry']

while (sel := input("Please select flavor").lower()) not in flavor:
    print(f"{sel} not available")

print("thanks")

