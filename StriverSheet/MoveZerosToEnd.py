def moveZero(arr):
    n = len(arr)
    temp = [0]*n
    j = 0
    for i in range(n):
        if arr[i]!=0:
            temp[j] = arr[i]
            j += 1
    return temp

def moveZeroOptimal(arr1):
    n = len(arr1)
    count = 0
    for i in range(n):
        if arr1[i]!=0:
            arr1[count] = arr1[i]
            count += 1
    while(count<n):
        arr1[count] = 0
        count += 1
    return arr1
    
        
                                                                 

arr1 = [0,3,4,6,0,0,5,0,34,67,4,0]
print(moveZeroOptimal(arr1))