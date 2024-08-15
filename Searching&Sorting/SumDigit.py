def sumDigit(n):
    if n == 0:
        return 0
    return (n%10 + sumDigit(n//10)) 

print(sumDigit(9))