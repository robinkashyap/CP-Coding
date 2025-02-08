def merge(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    arr =[m+n]*0
    i,j=0,0
    while(i<m and j<n):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while(i<m):
        arr.append(arr1[i])
        i+=1
    while(j<n):
        arr.append(arr2[j])
        j+=1
    return arr

arr1 = [3, 4, 10, 16, 17]
arr2 = [-8, 10, 12, 13]

result = merge(arr1, arr2)
print(result)
