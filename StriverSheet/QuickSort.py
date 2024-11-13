def partition(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while(i<j):
        while(arr[i]>=pivot and i <= high-1):
            i = i + 1
        while(arr[j]<pivot and j >= low+1):
            j = j - 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low],arr[j] = arr[j], arr[low]
    return j


def quickSort(arr,low,high):
    if (low<high):
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 1, 9]
# arr = [3,3,3,3,3,3]
quickSort(arr, 0, len(arr) - 1)
print(arr)