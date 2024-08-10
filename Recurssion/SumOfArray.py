def sumArray(arr, n):
    if n <= 0:
        return 0
    else:
        return sumArray(arr, n-1) + arr[n-1]

arr=[1,2,3,4,5]
result = sumArray(arr, 5)
print(result)
