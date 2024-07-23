# Time Complexity - O(n^2)
# Space Complexity - O(1)

# Selection sort is a simple and efficient sorting algorithm that works by repeatedly \n
# selecting the smallest (or largest) element from the unsorted portion of the list \n
# and moving it to the sorted portion of the list. 

# Not Stable (Does not preserve the relative order of items with equal keys) and Minimal memory usage


def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 22]
selectionSort(arr)
print("Sorted array:")
print("[",end="")
for i in range(len(arr)):
    if i == len(arr) - 1:
        print(f'{arr[i]}]')  # Print the last element without a comma
    else:
        print(f'{arr[i]}',end=",")