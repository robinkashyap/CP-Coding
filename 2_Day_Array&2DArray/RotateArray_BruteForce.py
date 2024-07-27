# Time Complexity - O(n+d)
# Space Complexity - O(d)

# rotate the array by d
# Step 1 - Store the array element in temp
# Step 2 - Shift the array element 
# Step 3 - Add the temp element to the last

def arrayRotate(arr,d):
    n = len(arr)
    d = d%n
    temp = [0]*d
    for i in range(d):                  #O(d)
        temp[i] = arr[i]
    for j in range(n-d):                #O(n-d)
        arr[j] = arr[d+j]
    for k in range(n-d,n):              #O(d)
        arr[k] = temp[k-(n-d)]
    return arr



# Time Complexity - O(n)
# Space Complexity - O(n)


# def arrayRotate(arr,d):
#     n = len(arr)
#     d = d%n
#     arr = arr[d:] + arr[:d]             #arr[d:] - O(n-d), arr[:d] - O(d)   
#     return arr




arr = [1, 2, 3, 4, 5, 6, 7]
d = 4
result = arrayRotate(arr,d)
print(result)
   
