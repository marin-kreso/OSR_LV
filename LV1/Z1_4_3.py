numbers = []

while True:
    number = input("Enter a number: ")
    if number == "Done":
        break
    try:
        number = int(number)
        numbers.append(number)
    except ValueError:
        print("Please enter a number!")

if numbers:
    print("Length:", len(numbers))
    print("Min:", min(numbers))
    print("Max:", max(numbers))
    print("Average:", sum(numbers)/len(numbers))

    numbers.sort()
    print(numbers)