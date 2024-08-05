# Time Complexity - O(n)
# Space Cmplexity - O(1)

# Swap the alternate number in array


def swapAlternate(arr):
    n = len(arr)
    for i in range(1,n,2):
        temp = arr[i]
        arr[i] = arr[i-1]
        arr[i-1] = temp
    return arr


arr = [1, 0, 2, 2, 1, 0, 1, 2, 1, 0]
result = swapAlternate(arr)
print(result)