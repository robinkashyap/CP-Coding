def removeDup(st):
    if len(st) == 0 or len(st) == 1:
        return st
    if st[0] == st[1]:
        result = removeDup(st[1:])
        return result
    else:
        result = removeDup(st[1:])
        return st[0] + result


st = 'aabbbccccddddde'
print(removeDup(st))