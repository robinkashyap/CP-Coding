def pushingZero(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while(count<n):
        arr[count] = 0
        count += 1
    return arr

arr = [3, 4, 0, 16, 0, 0, 17]
arr1 = [0,0,0,0,0,0,0]
arr2 = [1,2,3,4,5,6]
result = pushingZero(arr2)     
print(result)