def removeDuplicate(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[i]!=arr[j]:
            i = i+1
            arr[i] = arr[j]
    return i + 1

arr=[1,1,2,2,2]
result = removeDuplicate(arr)
for i in range(result):
    print(arr[i],end=' ')