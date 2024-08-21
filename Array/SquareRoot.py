number = 49
sqrt_number = int(number ** 0.5)  # This gives the integer part of the square root

square = sqrt_number * sqrt_number

if square == number:
    print(f"{number} is a perfect square, and its square root is {sqrt_number}.")
else:
    print(f"{number} is not a perfect square.")  