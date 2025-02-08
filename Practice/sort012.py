def sort012(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n-1
    while(mid<=high):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high-=1
    return arr
arr = [1, 0, 2, 2, 1, 0, 1, 2, 1, 0,0,1]
result = sort012(arr)
print(result)