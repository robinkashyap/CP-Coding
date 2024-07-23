# Time Complexity - {Best - O(n), Average and Worst - O(n^2) 
# Space Complexity - O(1)

# Swapping the adjacent elements if they are in the wrong order
# or
# Push the max element to right side by swapping

# This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# Simple and Stable (meaning that elements with the same key value maintain their relative order in the sorted output.)


def bubbleSort(arr):
    n = len(arr) - 1
    for i in range(n):
        swap = False
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if swap == False:
            break
 
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array:")
print("[",end="")
for i in range(len(arr)):
    if i == len(arr) - 1:
        print(f'{arr[i]}]')  # Print the last element without a comma
    else:
        print(f'{arr[i]}',end=",")

