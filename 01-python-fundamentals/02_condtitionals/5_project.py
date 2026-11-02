order_amount = int(input("Enter the order amount : "))

delivery_fees = 0 if order_amount < 300 else 30

total_amount = order_amount + delivery_fees

print(f"please pay  , {total_amount} to me")