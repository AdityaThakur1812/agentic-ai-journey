cup = input("Please enter the cup size (small/medium/large) :")
cup.lower()

if cup == "small":
    print("Pay me 10 ruppees")
elif cup == "medium":
    print("Pay me 15 ruppees")
elif cup == "large":
    print("Pay me 20 ruppees")
else:
    print("Unknown cup size")
