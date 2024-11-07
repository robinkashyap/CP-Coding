# get the min element in the array and place in its actual position
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        temp = i
        for j in range(i+1,n):
            if arr[temp] > arr[j]:
                temp = j
        arr[i],arr[temp] = arr[temp], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 9]
print(selectionSort(arr))
