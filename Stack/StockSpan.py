def stockSpan(price):
    n = len(price)
    span = [0]*n
    stack = []
    for i in range(n):
        while len(stack)>0 and price[stack[-1]]<price[i]:
            stack.pop()
        if not stack:   #check stack is empty or not
            span[i] = i+1
        else:
            span[i] = i - stack[-1]
        stack.append(i)
    return span

arr = [10,10,10,10]
result = stockSpan(arr)
print(result)