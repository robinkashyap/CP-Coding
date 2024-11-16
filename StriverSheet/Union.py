def union(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    union = []
    i,j = 0,0
    while(i<n1 and j<n2):
        if arr1[i]<=arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    while(i<n1):
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
    while(j<n2):
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union

arr1 = [1,2,3,4,4,5,6]
arr2 = [2,2,2,4,5,6,8,9]
print(union(arr1,arr2))
         