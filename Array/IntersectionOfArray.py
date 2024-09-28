# Intersection of two arrays

def merging(arr1,arr2,m,n):
    arr = []
    i = 0
    j = 0
    while(i<m and j<n):
        if arr1[i]<arr2[j]:
            i = i + 1
        elif arr1[i] == arr2[j]:
            arr.append(arr1[i])
            i = i + 1
            j = j + 1
        else:
            j = j + 1
    return arr

arr1 = [3, 4, 10, 12, 17]
arr2 = [8, 10, 12, 13]

result = merging(arr1, arr2,5,4)
print(result)

