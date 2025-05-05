def swap(a,b):
    a = a + b # 10 + 20 = 30
    b = a - b # 30 - 20 = 10
    a = a - b # 30 - 10 = 20
    print(f'a = {a}')
    print(f'b = {b}')
a = 10
b = 20
swap(a,b)