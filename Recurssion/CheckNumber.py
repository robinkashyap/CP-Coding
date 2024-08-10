def checkNumber(arr, n, k):
    if n > 0:
        if arr[n-1] == k:
            return True
        else:
            return checkNumber(arr, n-1, k)
    else:
        return False
arr=[1,2,3,4,5]
result = checkNumber(arr, 5, 0)
print(result)