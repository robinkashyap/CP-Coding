# Time Complexity = O(log(n)) - for both code

# Code 1
def countZeros(n):
    if n == 0:
        return 1
    if (n<10 and n!=0):
        return 0
    return countZeros(n//10) + (n%10 == 0)

# Code 2

def countZero1(n):
    if n == 0:
        return 1
    return helper(n)

def helper(n):
    if n == 0:
        return 0
    if n%10 == 0:
        return 1 + helper(n//10)
    else:
        return helper(n//10)


print(countZeros(0))