def removeChar(st):
    if len(st) == 0:
        return st
    result = removeChar(st[1:])
    if st[0] == 'x':
        return result
    else:
        return st[0] + result
    
st = 'daxdxxd'
print(removeChar(st))