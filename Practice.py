def counting1(arr):
    n = len(arr)
    max_count = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    
    return count
                
        
arr = [1,1,1,1,0,3,4,1,1,2,1,1,1,1,1,1,1]
arr1 = [0,0,0,0,0,0,0]
arr2 = [1,1,1,1,1,1,1]
print(counting1(arr2))
