
# Remove Duplicates in-place from Sorted Array

# Brute force approach is - put the elements in set and then replace the unique element in the array
# Time Complexity - O(N log N + N)
# Space Complexity - O(N)

# We are following Optimal Approach - Two Pointer

def removeDuplicate(arr):
    n = len(arr)
    i = 0                   # we know that first element is unique so we don't need to change the position
    for j in range(i+1,n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i = i + 1
    return i+1

# arr = [1, 1, 1, 2, 5, 5, 6, 10, 30]
# arr = [1, 2, 3, 4, 5, 6]
arr = [5, 5, 5, 5, 5, 5]
result = removeDuplicate(arr)
print("[",end="")
for i in range(result):
    if i == result - 1:
        print(f'{arr[i]}]',end="")
    else:
        print(arr[i],end=",")