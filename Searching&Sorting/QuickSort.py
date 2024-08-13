# Time Complexity - O(n log n)
# Space Complexity - O(1)

# Quick Sort - Divide and Conquer 
# Pick a Pivot and place it on the the correct place in the sorted array
# smaller on the left and larger on the right


def partition(ar, low, high):
    pivot = ar[low]
    i = low
    j = high
    while(i<j):
        while(ar[i] <= pivot and i <= high - 1):
            i += 1
        while(ar[j] > pivot and j >= low + 1):
            j -= 1 
        if i < j:
            ar[i], ar[j] = ar[j], ar[i]
    ar[j], ar[low] = ar[low], ar[j]
    return j


def quickSort(ar, low, high):
    if low < high:
        p = partition(ar, low, high)
        quickSort(ar,low,p-1)
        quickSort(ar,p+1,high)


# arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 1, 9]
arr = [3,3,3,3,3,3]
quickSort(arr, 0, len(arr) - 1)
print(arr)