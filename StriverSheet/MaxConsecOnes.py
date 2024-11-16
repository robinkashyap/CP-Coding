def maxConsecOnes(arr):
    n = len(arr)
    max,count = 0,0
    for i in range(n):
        if arr[i]==1:
            count+=1
        else:
            if count>max:
                max = count
            count = 0
    if count>max:
        max = count
    return max

arr = [1,1,1,1,1,1,1,1]                                                                   
print(maxConsecOnes(arr))