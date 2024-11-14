def shiftLeft(arr):
    n = len(arr)
    temp = [0]*n
    for i in range(1,n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]
    for i in range(n):
        print(temp[i],end =" ")

def shiftLeftOptimal(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[i] = temp
    return arr

arr = [3,5,1,4,6,7]
print(shiftLeftOptimal(arr))
        