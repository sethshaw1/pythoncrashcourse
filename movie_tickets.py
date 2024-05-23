
while True:
    age = input("What's your age?")
    age = int(age)
    if age < 3:
        print("$3")
    elif age < 12:
        print("$8")
    elif age == "quit":
        break
    else:
        print("$20")