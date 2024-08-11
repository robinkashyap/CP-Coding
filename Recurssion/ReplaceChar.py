def replaceChar(st, ch1, ch2):
    n = len(st)
    if n == 0:
        return st
    result = replaceChar(st[1:],ch1,ch2)
    if st[0]==ch1:
        return ch2 + result
    else:
        return st[0] + result

st = 'daxdxxd'
print(replaceChar(st, 'x', 'c'))
