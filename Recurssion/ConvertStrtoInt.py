def convert(s):
    n = len(s)
    if n == 0:
        return 0
    return convert(s[:n-1]) * 10 + (ord(s[-1]) - ord('0'))

s = '0002340'
result = convert(s)
print(result)
