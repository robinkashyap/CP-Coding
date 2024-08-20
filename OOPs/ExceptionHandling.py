while True:
    try:
        n = input("Enter the numerator: ")
        num = int(n)
        n = input("Enter the denominator: ")
        denom = int(n)
        value = num/denom
        print(value)
        break
    except ValueError:
        print("Numerator and Denominator should be integer")
