# Time Complexity - {Best - O(n), Average and Worst - O(n^2)
# Space Complexity - O(1)

# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element \n
# of an unsorted list into its correct position in a sorted portion of the list.

# Stable and efficient for partial order 


def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp

arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 22] 
# 34,64,25
insertionSort(arr)
print("Sorted array:")
print("[",end="")
for i in range(len(arr)):
    if i == len(arr) - 1:
        print(f'{arr[i]}]')  # Print the last element without a comma
    else:
        print(f'{arr[i]}',end=",")