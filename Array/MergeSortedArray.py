# Time Complexity - O(m+n)
# Space Complexity - O(m+n)

# Merge two sorted array in third array


def mergeArray(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    arr = [0]*(m+n)
    i = 0
    j = 0
    idx = 0
    while(i < m and j < n):
        if arr1[i] < arr2[j]:
            arr[idx] = arr1[i]
            i = i + 1
            idx = idx + 1
        else:
            arr[idx] = arr2[j]
            j = j + 1
            idx = idx + 1
    while(i < m):
        arr[idx] = arr1[i]
        i = i + 1
        idx = idx + 1
    while(j < n):
        arr[idx] = arr2[j]
        j = j + 1
        idx = idx + 1
    return arr

arr1 = [3, 4, 10, 16, 17]
arr2 = [8, 10, 12, 13]

result = mergeArray(arr1, arr2)
print(result)
