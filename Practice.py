def binarySearch(arr,low,high,k):
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid]>=k:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1,3,4,6,10,12,23,45,67,90,100,101]
print(binarySearch(arr,0,len(arr)-1,12))