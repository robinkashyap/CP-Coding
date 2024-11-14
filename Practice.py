def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
            
    return arr

arr = [64, 34, 25, 12, 22, 11, 90, 25, 64, 22, 9] # 64,64
print(insertionSort(arr))
            