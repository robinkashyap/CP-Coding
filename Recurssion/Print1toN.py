
def print1_N(n):
    if n == 0:
        return 
    print1_N(n-1)
    print(n)
    return

n = 10
print1_N(n)