device_status = input("Give me device status").lower()

temp = int(input("temperature : "))

if device_status == "active":
    if temp > 35:
        print("Temperature too high")
    else:
        print("Temperature is normal")
else:
    print("Device is not active")
