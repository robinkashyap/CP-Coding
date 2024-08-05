# Time Complexity - O(n)
# Space Complexity - O(1)

# Sort the array of 0,1,2 

def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while(mid<=high):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            mid = mid + 1
            low = low + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high = high - 1
    return arr

arr = [1, 0, 2, 2, 1, 0, 1, 2, 1, 0]
result = sort012(arr)
print(result)