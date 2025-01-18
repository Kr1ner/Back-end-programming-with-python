def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print(f"Error: the value is not within permitted range ({min}..{max})")
        except ValueError:
            print("Error: wrong input")

v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
