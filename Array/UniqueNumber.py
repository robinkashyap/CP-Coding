# Time Complexity - O(n^2)
# Space Complexity - O(1)

# Find the unique number in array


def unique(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i]==arr[j]:
                count = count + 1
        if count == 1:
            return arr[i]

                

arr = [1, 3, 1, 3, 6, 6, 7, 10, 7]
result = unique(arr)
print(result)