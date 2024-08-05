# Time Complexity - O(log n)
# Space Complexity - O(1)

# Array should be sorted


def binarySearch(arr,low,high,k):
    while(low <= high):
        mid = low + (high-low)//2  #expression is to prevent integer overflow (if the sum exceeds the maximum value that an integer can hold)
        if arr[mid] == k:
            return mid
        elif arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1
    return 0

arr = [10,13,24,76,123,155,189]
x = 176
result = binarySearch(arr,0,len(arr),x)
if result == 0:
    print(f'{x} is not present inside the array')
else:
    print(f'{x} is present inside the array at position {result}')

    