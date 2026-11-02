seat_type = input("Please select a seat type (Sleeper/AC/General/Luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("No AC ,but beds are available")
    case "ac":
        print("Fully Air Conditioned")
    case "general":
        print("No reservation")
    case "luxury":
        print("super comfy with AC")
    case _:
        print("invalid seat type")