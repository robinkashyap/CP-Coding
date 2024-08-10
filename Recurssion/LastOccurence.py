# Given an array of length N and an integer x, 
# you need to find and return the last index of integer x present in the array. 
# Return -1 if it is not present in the array.


# def lastNumberIndex(arr,k, si):
#     if si < 0:
#         return -1
#     if arr[si] == k:
#         return si
#     else:
#         return lastNumberIndex(arr, k, si-1)


# def lastNumberIndex(arr, x, si,count):
#     n = len(arr)
#     if si < n:
#         if si == n:
#             return -1
#         if arr[si] == x:
#             count = si
#         return lastNumberIndex(arr, x, si+1,count)
#     else:
#         return count

def lastNumberIndex(arr, x, si):
    n = len(arr)
    if si == n:
         return -1
    result = lastNumberIndex(arr, x, si+1)
    if result!= -1:
        return result
    else:
        if arr[si]==x:
            return si
        else:
            return -1


arr=[6,1,1,1,1,0,1]
result = lastNumberIndex(arr, 6, 0)
print(result)