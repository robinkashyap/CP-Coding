def intersection(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    union = []
    i,j = 0,0
    while(i<n1 and j<n2):
        if arr1[i]==arr2[j]:
            union.append(arr1[i])
            i += 1
            j += 1
        else:
            if arr1[i] < arr2[j]:
                i+=1
            else:
                j+=1
    return union

arr1 = [1,2,3,4,4,5,6]
arr2 = [2,2,2,4,5,6,8,9]
print(intersection(arr1,arr2))