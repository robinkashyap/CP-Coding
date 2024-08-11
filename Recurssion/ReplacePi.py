def replacePi(st):
    n = len(st)
    pi = '3.14'
    if n == 0 or n == 1:
        return st
    if st[0] == 'p' and st[1] == 'i':
        result = replacePi(st[2:])
        return pi + result
    else:
        result = replacePi(st[1:])
        return st[0] + result

st = 'dpippi'
print(replacePi(st))
