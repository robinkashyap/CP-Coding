# Time Complexity - O(n)
# Space Complexity - O(1)

# Given an array of size n, write a program to check if the given array is sorted in \n
# (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.


def arraySorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            return False
    return True

# arr = [0, -1, 2, -3, 1, 50, 100, 100]
arr = [-3, -1, 0, 1, 2, 50, 100, 100]
result = arraySorted(arr)
print(result)
