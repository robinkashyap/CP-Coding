def top(stack):
    return stack[len(stack)-1]

def minReversal(exp):
    if len(exp)%2!=0:
        return -1
    stack = []
    for ele in exp:
        if ele == '{':
            stack.append(ele)
        else:
            if(len(stack)>0 and top(stack) == '{'):
                stack.pop()
            else:
                stack.append(ele)
    a,b=0,0
    while (len(stack)>0):
        if(top(stack)=='{'):
            b+=1
        else:
            a+=1
        stack.pop()
    ans = (a+1)//2 + (b+1)//2
    return ans

exp = '}{'
print(minReversal(exp))