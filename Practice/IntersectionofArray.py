def inter(arr1,arr2):
    arr = []
    m = len(arr1)
    n = len(arr2)
    i,j = 0,0
    while(i<m and j<n):
        if arr1[i] == arr2[j]:
            arr.append(arr1[i])
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return arr

arr1 = [3, 4, 10, 12, 17]
arr2 = [8, 10]

result = inter(arr1, arr2)
print(result)