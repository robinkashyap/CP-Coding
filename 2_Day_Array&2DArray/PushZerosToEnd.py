# Time Complexity - O(n)
# Space Complexity - O(1)

# push all zeros to end


def pushZeros(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i]!=0:
            arr[count] = arr[i]
            count = count + 1
    while(count < n):
        arr[count] = 0
        count = count + 1
    return arr

arr = [3, 4, 0, 16, 0, 0, 17]
result = pushZeros(arr)     
print(result)