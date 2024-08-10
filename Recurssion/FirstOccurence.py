# Given an array of length N and an integer x, 
# you need to find and return the first index of integer x present in the array. 
# Return -1 if it is not present in the array.


def firstNumberIndex(arr,si, k):
    n = len(arr)
    if si == n:
        return -1
    if arr[si] == k:
        return si
    else:
        return firstNumberIndex(arr, si+1 , k)

arr=[1,2,3,3,4,3]
result = firstNumberIndex(arr, 0, 3)
print(result)