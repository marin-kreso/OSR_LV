try:
    number = float(input("Enter a number: "))

    if number < 0.0 or number > 1.0:
        raise ValueError

    if number < 0.6:
        print("F")
    elif number < 0.7:
        print("D")
    elif number < 0.8:
        print("C")
    elif number < 0.9:
        print("B")
    else:
        print("A")

except ValueError:
    print("Number must be between 0 and 1 or input is not a number.")