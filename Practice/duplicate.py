def removeDup(arr):
    n = len(arr)
    i = 0
    for j in range(i+1,n):
        if arr[j]!=arr[i]:
            arr[i+1] = arr[j]
            i+=1
    return i

arr = [1, 1, 1, 2, 5, 5, 6, 10, 30]
res = removeDup(arr)
for i in range(res+1):
    print(arr[i],end=" ")