def listSorted(arr,si):
    n = len(arr)
    if si == n-1 or si == n:
        return True
    if arr[si] > arr[si+1]:
        return False
    else:
        return listSorted(arr,si+1)

arr = []
result = listSorted(arr,0)
print(result)