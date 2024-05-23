
while True:
    message = input("What topping would you like on your pizza?: ")
    print("(Type quit to finish)")
    if message == "quit":
        break
    else:
        print(f"We'll add {message} to your pizza.")