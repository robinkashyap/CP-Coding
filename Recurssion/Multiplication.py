def multiplication(n,m):
    if n == 0 or m == 0:
        return 0
    if n>0:
        return n + multiplication(n,m-1)
    else:
        return multiplication(n,m+1) - n


print(multiplication(3,4))