def countBracketReversals(exp):
    n = len(exp)
    if n%2 != 0:
        return -1
    a = 0
    b = 0
    for i in exp:
        if i == '{':
            a+=1
        else:
            b+=1
    return abs(a-b)//2
    
