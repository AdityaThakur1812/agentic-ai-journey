user_choice = input("Please enter the snack")
user_choice.lower()

if user_choice == "samosa" or user_choice == "cookies":
    print("Great choice we will server you ", user_choice)
else: 
    print("Sorry we only server samosa and cookies ")
