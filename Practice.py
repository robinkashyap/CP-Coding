def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                swap = True
                arr[j],arr[j+1] = arr[j+1], arr[j]
        if swap == False:
            break
    return arr

arr = [64, 34, 25, 12, 100, 100, 90]
print(bubbleSort(arr))