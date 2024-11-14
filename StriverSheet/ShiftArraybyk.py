def shiftRight(arr,k):
    n = len(arr)
    temp =[0]*n
    p = 0
    for i in range(n-k,n):
        temp[p] = arr[i]
        p += 1
    for j in range(n-k):
        temp[p] = arr[j]
        p += 1
    return temp

def shiftLeft(arr,k):
    n = len(arr)
    temp = [0]*n
    p = 0
    for i in range(k,n):
        temp[p] = arr[i]
        p+=1
    for j in range(k):
        temp[p] = arr[j]
        p+=1
    return temp

arr = [1,2,3,4,5,6,7]
k = 4
print(shiftRight(arr,k))
print(shiftLeft(arr,k))

