def lastNumberIndex(arr, x):
    n = len(arr)
    si = -1
    for i in range(n):
        if arr[i] == x:
            si = i
    return si

arr = [34, 57, 82, 41, 65, 35, 82, 27, 36, 12, 6, 40, 66, 99, 25, 29, 22, 25, 12, 24, 65, 15, 5, 43, 28, 33, 76, 32, 13, 95, 22, 84, 71, 23, 28, 7, 65, 94, 18, 47, 9, 42, 61, 73] 
x = 61
print(lastNumberIndex(arr, x))