# Time Complexity - O(n)
# Space Complexity - O(1)

# Find the Second Largest element in an array


def largestElement(arr):
    n = len(arr)
    if n < 1:
        return 0
    elif n == 1:
        return -1
    else:
        max_1 = arr[0]
        max_2 = arr[0]
        for i in range(n):
            if max_1 < arr[i]:
                max_2 = max_1
                max_1 = arr[i]
        return max_2

arr = [0, -1, 2, -3, 1, 50, 100, 100]
result = largestElement(arr)
if result == 0:
    print("No element is present in the array")
elif result == -1:
    print("Minimum two element is needed in the array")
else:
    print(f'Second largest element in the array is {result}')
