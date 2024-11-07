# check the adjacent elements if larger then swap

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(1,n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swap = True
        if swap == False:
            break
    return arr


arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 9]
print(bubbleSort(arr))
