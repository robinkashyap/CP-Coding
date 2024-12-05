def fib(n):
    if n<= 0:
        return -1
    elif n == 1:
        return 1
    n1 = 0
    n2 = 1
    n3 = n2
    for i in range(1,n):
        if i == 1:
            print(n3,end=' ')
        print(n3,end=' ')
        n1 = n2
        n2 = n3
        n3 = n1 + n2

fib(1)