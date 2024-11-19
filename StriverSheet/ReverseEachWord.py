def reverse(arr,start,end):
    while(start<=end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def reverseWord(str1):
    arr = list(str1)
    n = len(arr)
    i,l = 0,0
    j = n-1
    for i in range(n):
        if arr[i] == ' ':
            reverse(arr,l,i-1)
            l = i + 1
    reverse(arr,l,n-1)
    return ''.join(arr)

def reverseWordstr(str1):
    arr = list(str1)
    n = len(arr)
    i,l = 0,0
    j = n-1
    for i in range(n):
        if arr[i] == ' ':
            reverse(arr,l,i-1)
            l = i + 1
    reverse(arr,l,n-1)
    
    return ''.join(arr)


str = 'My name is Nonu'
print(reverseWord(str))