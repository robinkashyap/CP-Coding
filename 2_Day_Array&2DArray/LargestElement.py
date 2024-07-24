# Time Complexity - O(n)
# Space Complexity - O(1)

# Find the Largest element in an array


def largestElement(arr):
    n = len(arr)
    if n < 1:
        return 0
    else:
        max = arr[0]
        for i in range(n):
            if max < arr[i]:
                max = arr[i]
        return max

arr = [50]
result = largestElement(arr)
if result == 0:
    print("No element is present in the array")
else:
    print(f'largest element in the array is {result}')    