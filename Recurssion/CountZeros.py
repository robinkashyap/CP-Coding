def countZeros(n):
    if n == 0:
        return 1
    if (n<10 and n!=0):
        return 0
    return countZeros(n//10) + (n%10 == 0)

print(countZeros(10200))